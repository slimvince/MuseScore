<#
.SYNOPSIS
  TRUE per-branch coverage for the composing L1-L4 module (src/composing/analysis),
  using a clang-cl-instrumented `composing_analysis` linked against the EXISTING
  MSVC build. Measurement-only; additive; the production MSVC/ninja build, the BIR
  gate, and the snapshot goldens are all UNTOUCHED.

  UNION mode (default): the ONE instrumented `composing_analysis` lib is relinked
  into BOTH `composing_tests` and `notation_tests`; each suite runs under
  instrumentation -> two .profraw; `llvm-profdata merge` combines them into the
  UNION profile -> the whole-corpus L1-L4 branch%. `notation_tests` is the suite
  hypothesized to drive the three composing files `composing_tests` leaves at 0%
  (sectionanalyzer / sectioncadencedetection / keymodeformatting). Pass
  -ComposingOnly to reproduce the original single-suite (composing_tests) report.

.DESCRIPTION
  OpenCppCoverage (tools/coverage/run_coverage.ps1) is LINE-only: its cobertura
  export carries no per-branch data (branches-valid="0"). Criterion 4 ("every branch
  hit at least once") needs real branch coverage. clang's instrumentation + llvm-cov
  --show-branches=count is the path.

  The CHEAP path (no full Qt-under-clang rebuild, no production source edits):
    1. Read the EXISTING MSVC ninja build's compile DB and link command (read-only).
    2. Recompile ONLY the 3 composing_analysis unity TUs with clang-cl, reusing the
       production flags verbatim, adding -fprofile-instr-generate -fcoverage-mapping.
       (Drops the MSVC PCH /Yu+/Fp -- clang-cl cannot read an MSVC .pch -- but keeps
       the /FI force-include so the code still sees the PCH header contents.)
    3. Archive the instrumented objects into composing_analysis_instr.lib (llvm-lib).
    4. Relink composing_tests by reusing the production link command verbatim, with
       three surgical swaps: composing_analysis.lib -> the instrumented lib; /out
       /implib /pdb -> the coverage out dir (production binary untouched); + the
       clang_rt.profile runtime. The linker is swapped MSVC link.exe -> lld-link:
       clang's profile sections are located at runtime via linker-defined $A/$Z
       boundary symbols on grouped sections, which MSVC link.exe lays out wrongly
       ("malformed instrumentation profile data: symbol name is empty" on merge);
       lld-link handles them. It is a drop-in MSVC-compatible linker -- same args,
       same MSVC-built objects/libs.
    5. Run the existing composing_tests suite under instrumentation (Qt resolves via
       the install on PATH; the test data root is an absolute compile-time path).
    6. llvm-profdata merge -> llvm-cov report/show/export scoped to L1-L4.

  Why it works: clang-cl emits MSVC-ABI COFF objects with MSVC name mangling, so the
  instrumented composing_analysis links seamlessly with the MSVC-compiled test
  objects + engraving/muse/Qt/gtest libs. Only composing_analysis is instrumented,
  so only its sources carry coverage mapping -> the report is naturally scoped to
  L1-L4. Verified 2026-06-26 with LLVM 22.1.8 against MSVC 14.42 / Qt 6.10.1.

  PREREQUISITES (all no-admin):
    - Portable LLVM in $LlvmBin (clang-cl, llvm-lib, lld-link, llvm-profdata,
      llvm-cov, and lib/clang/<v>/lib/windows/clang_rt.profile-x86_64.lib). Install:
      extract LLVM-<ver>-win64.exe (NSIS) with 7-Zip into a stable dir.
    - The production MSVC build already built in $BuildDir (so composing_tests' MSVC
      objects + all link libs exist). This script never invokes the production build.

.EXAMPLE
  pwsh -File tools\coverage\run_branch_coverage.ps1
#>
param(
  [string]$Repo     = 'C:\s\MS',
  [string]$BuildDir = 'C:\s\MS\ninja_build_rel',
  [string]$LlvmBin  = 'C:\Users\vince\tools\LLVM\bin',
  [string]$Vcvars   = 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat',
  [string]$Ninja    = 'C:\Qt\Tools\Ninja\ninja.exe',
  [string]$OutDir   = 'C:\s\MS\scratch_artifacts\coverage\clang_branch',
  [switch]$ComposingOnly   # default OFF -> UNION (composing_tests + notation_tests)
)

$ErrorActionPreference = 'Stop'
function Fail($m) { Write-Error $m; exit 2 }

$clangcl  = Join-Path $LlvmBin 'clang-cl.exe'
$llvmlib  = Join-Path $LlvmBin 'llvm-lib.exe'
$lldlink  = Join-Path $LlvmBin 'lld-link.exe'
$profdataExe = Join-Path $LlvmBin 'llvm-profdata.exe'
$covExe   = Join-Path $LlvmBin 'llvm-cov.exe'
foreach ($t in @($clangcl,$llvmlib,$lldlink,$profdataExe,$covExe,$Ninja,$Vcvars)) {
  if (-not (Test-Path $t)) { Fail "missing tool: $t" }
}
$profLib = Get-ChildItem -Path (Join-Path $LlvmBin '..\lib\clang') -Recurse -Filter 'clang_rt.profile-x86_64.lib' -ErrorAction SilentlyContinue |
           Select-Object -First 1 -ExpandProperty FullName
if (-not $profLib) { Fail "clang_rt.profile-x86_64.lib not found under $LlvmBin\..\lib\clang" }

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$objDir = Join-Path $OutDir 'instr_obj'
New-Item -ItemType Directory -Force -Path $objDir | Out-Null

# Run native command lines under a vcvars64 environment (compile/link need MSVC
# headers/libs + the Windows SDK). The BATCH self-redirects every command's stdout
# and stderr to the log file -- so cmd.exe emits nothing back to PowerShell. This
# avoids PS 5.1's NativeCommandError trap, where a native tool writing warnings to
# stderr is wrapped as a terminating error under $ErrorActionPreference='Stop'.
# Returns the exit code of the LAST command (correctness is additionally gated by
# the object/exe existence checks at each call site).
function Invoke-UnderVcvars([string[]]$CmdLines, [string]$LogPath) {
  $L = "`"$LogPath`""
  $redir = $CmdLines | ForEach-Object {
    if ($_ -match '^\s*echo ') { "$_ >> $L" } else { "$_ >> $L 2>&1" }
  }
  $lines = @('@echo off', "call `"$Vcvars`" >nul 2>&1", "cd /d `"$BuildDir`"",
             "if exist $L del $L") + $redir + "(echo VCV_EXIT:%ERRORLEVEL%)>> $L"
  $bat = Join-Path $OutDir '_run.bat'
  Set-Content -Path $bat -Value ($lines -join "`r`n") -Encoding ascii
  cmd.exe /c "`"$bat`"" | Out-Null
  $m = Select-String -Path $LogPath -Pattern 'VCV_EXIT:(\d+)' | Select-Object -Last 1
  if ($m) { return [int]$m.Matches[0].Groups[1].Value } else { return 1 }
}

# clang-cl translation of a production cl.exe compile command for one unity TU.
function Translate-Compile([string]$cmd, [string]$objOut) {
  $cmd = $cmd.Trim()
  $cmd = $cmd -replace '^\S*cl\.exe', "`"$clangcl`""   # compiler
  $cmd = $cmd -replace '/Yu\S+', ''                      # drop MSVC PCH use
  $cmd = $cmd -replace '/Fp\S+', ''                      # drop MSVC PCH file
  $cmd = $cmd -replace '-external:I', '/I'               # Qt external includes -> /I
  $cmd = $cmd -replace '\s-external:W0\s', ' '
  $cmd = $cmd -replace '/showIncludes', ''               # ninja dep noise
  $cmd = $cmd -replace '\s-Zi\s', ' '                    # skip PDB (coverage map is independent)
  $cmd = $cmd -replace '\s/MP\s', ' '
  $cmd = $cmd -replace '/Fd\S+', ''
  $cmd = $cmd -replace '\s/FS\s', ' '
  $cmd = $cmd -replace '\s-MD\s', ' /MD '                # normalize the one ambiguous CRT flag
  $cmd = $cmd -replace '/Fo\S+', "/Fo`"$objOut`""        # redirect object to OutDir
  return $cmd + ' -fprofile-instr-generate -fcoverage-mapping'
}

Write-Output "== 1. compile DB from the existing MSVC build (read-only) =="
$compdb = Join-Path $OutDir 'compdb.json'
& $Ninja -C $BuildDir -t compdb > $compdb 2>$null
$db = Get-Content $compdb -Raw | ConvertFrom-Json
$units = $db | Where-Object { $_.file -match 'composing/analysis' -and $_.output -match 'unity_\d+_cxx\.cxx\.obj$' }
if (-not $units) { Fail "no composing_analysis unity TUs in compile DB (is the MSVC build present and unity-enabled?)" }
Write-Output ("   {0} unity TUs" -f $units.Count)

Write-Output "== 2. recompile composing_analysis TUs with clang-cl + instrumentation =="
$objList = @()
$compileLines = @()
foreach ($u in $units) {
  $leaf = [System.IO.Path]::GetFileName($u.output)
  $obj  = Join-Path $objDir $leaf
  $objList += $obj
  $compileLines += "echo === $leaf ==="
  $compileLines += (Translate-Compile $u.command $obj)
}
$rc = Invoke-UnderVcvars $compileLines (Join-Path $OutDir 'compile.log')
if ($rc -ne 0) { Fail "clang-cl compile failed (rc=$rc); see $OutDir\compile.log" }
foreach ($o in $objList) { if (-not (Test-Path $o)) { Fail "missing object $o" } }

Write-Output "== 3. archive instrumented composing_analysis.lib =="
$instrLib = Join-Path $OutDir 'composing_analysis_instr.lib'
& $llvmlib "/OUT:$instrLib" @objList | Out-Null
if (-not (Test-Path $instrLib)) { Fail "llvm-lib failed" }

# Relink one test exe (MSVC-built) against the instrumented composing_analysis lib,
# swapping MSVC link.exe -> lld-link and redirecting /out /implib /pdb into OutDir so
# the production binary is never touched. Returns the path to the coverage exe.
# Works for any target whose link command links composing_analysis.lib (composing_tests,
# notation_tests) -- the four swaps (linker, lib, out, implib/pdb) are parameterized by
# $target; the composing_analysis.lib swap is the SAME instrumented lib for both suites.
function Relink-Test([string]$target) {
  $cmds = Join-Path $OutDir "$target`_commands.txt"
  & $Ninja -C $BuildDir -t commands $target > $cmds 2>$null
  $full = (Select-String -Path $cmds -Pattern "$target\.exe" |
           Where-Object { $_.Line -match "link\.exe|/out:$target\.exe" } | Select-Object -Last 1).Line
  if (-not $full) { Fail "could not find $target link command" }
  $m = [regex]::Match($full, '(?s) -- (.*?) && cd \.')
  $link = if ($m.Success) { $m.Groups[1].Value.Trim() } else { $full }
  $covExeOut = Join-Path $OutDir "$target`_cov.exe"
  $link = $link -replace '\S*link\.exe', "`"$lldlink`""                              # MSVC link.exe -> lld-link
  $link = $link -replace 'src\\composing\\analysis\\composing_analysis\.lib', "`"$instrLib`""
  $link = $link -replace "/out:$target\.exe", "/out:`"$covExeOut`""
  $link = $link -replace "/implib:\S*$target\.lib", "/implib:`"$(Join-Path $OutDir "$target`_cov.lib")`""
  $link = $link -replace "/pdb:$target\.pdb", "/pdb:`"$(Join-Path $OutDir "$target`_cov.pdb")`""
  $link = $link -replace '\s/INCREMENTAL\s', ' '
  $link = $link + " `"$profLib`""
  $rc = Invoke-UnderVcvars @($link) (Join-Path $OutDir "$target`_link.log")
  if ($rc -ne 0 -or -not (Test-Path $covExeOut)) { Fail "$target relink failed (rc=$rc); see $OutDir\$target`_link.log" }
  return $covExeOut
}

# Run an instrumented exe from $BuildDir (Qt + test-data roots resolve there), directing
# its coverage to $profraw. A nonzero test exit is a WARNING (a failing test still emits
# valid coverage); a MISSING .profraw is fatal (instrumentation didn't run).
function Run-Instrumented([string]$covExe, [string]$profraw, [string]$logName) {
  if (Test-Path $profraw) { Remove-Item $profraw -Force }
  $env:LLVM_PROFILE_FILE = $profraw
  Push-Location $BuildDir
  & $covExe > (Join-Path $OutDir $logName) 2>&1
  $rc = $LASTEXITCODE
  Pop-Location
  if ($rc -ne 0) { Write-Warning "$covExe exit=$rc (see $OutDir\$logName)" }
  if (-not (Test-Path $profraw)) { Fail "no .profraw emitted by $covExe" }
}

$src = Join-Path $Repo 'src\composing\analysis'

Write-Output "== 4. relink composing_tests (lld-link) against the MSVC build =="
$ctExe = Relink-Test 'composing_tests'

Write-Output "== 5. run composing_tests under instrumentation =="
$ctProfraw = Join-Path $OutDir 'composing.profraw'
Run-Instrumented $ctExe $ctProfraw 'composing_testrun.log'

# composing_tests-only report (the original single-suite baseline -- kept for the
# union delta / 0%-files comparison).
$ctProfdata = Join-Path $OutDir 'composing.profdata'
& $profdataExe merge -sparse $ctProfraw -o $ctProfdata
if (-not (Test-Path $ctProfdata)) { Fail "llvm-profdata merge (composing) failed" }
& $covExe report $ctExe "-instr-profile=$ctProfdata" $src "-show-branch-summary" > (Join-Path $OutDir 'composing_branch_report.txt') 2>&1

$profrawList = @($ctProfraw)

if (-not $ComposingOnly) {
  Write-Output "== 6. relink notation_tests (lld-link) against the SAME instrumented lib =="
  $ntExe = Relink-Test 'notation_tests'

  Write-Output "== 7. run notation_tests under instrumentation =="
  $ntProfraw = Join-Path $OutDir 'notation.profraw'
  Run-Instrumented $ntExe $ntProfraw 'notation_testrun.log'
  $profrawList += $ntProfraw
}

Write-Output "== 8. merge UNION + llvm-cov (report / export / html show) =="
# The union profile is keyed by coverage-mapping hash, so the SAME instrumented
# composing_analysis TUs (identical in both relinked exes) merge cleanly across suites.
$unionProfdata = Join-Path $OutDir 'union.profdata'
& $profdataExe merge -sparse @profrawList -o $unionProfdata
if (-not (Test-Path $unionProfdata)) { Fail "llvm-profdata merge (union) failed" }
# Report against whichever instrumented exe exists (the coverage mapping is identical);
# composing_tests_cov.exe is always present.
& $covExe report $ctExe "-instr-profile=$unionProfdata" $src "-show-branch-summary" > (Join-Path $OutDir 'union_branch_report.txt') 2>&1
& $covExe export $ctExe "-instr-profile=$unionProfdata" $src -format=text > (Join-Path $OutDir 'union_branch_export.json') 2>$null
& $covExe show   $ctExe "-instr-profile=$unionProfdata" $src "--show-branches=count" "-format=html" "-output-dir=$(Join-Path $OutDir 'union_html')" "-show-line-counts-or-regions" 2>$null

$ctTotal    = (Select-String -Path (Join-Path $OutDir 'composing_branch_report.txt') -Pattern '^TOTAL').Line
$unionTotal = (Select-String -Path (Join-Path $OutDir 'union_branch_report.txt') -Pattern '^TOTAL').Line
Write-Output "DONE. Outputs in $OutDir"
Write-Output ("composing_tests-only TOTAL: " + $ctTotal)
if (-not $ComposingOnly) { Write-Output ("UNION (composing + notation) TOTAL: " + $unionTotal) }
