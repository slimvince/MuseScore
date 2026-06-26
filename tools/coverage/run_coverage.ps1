<#
.SYNOPSIS
  Code-coverage runner for the `composing` module test backfill.

.DESCRIPTION
  Drives one of the project test binaries under OpenCppCoverage 0.9.9.0 and emits a
  cobertura XML (machine-parseable line coverage) plus an HTML report, filtered to
  `src\composing` sources.

  IMPORTANT — tool capability (verified 2026-06-26):
    OpenCppCoverage measures LINE / instruction coverage only. Its cobertura export
    carries NO per-branch data (branches-valid="0"; every <line> has only `hits`),
    and its HTML marks each line covered/uncovered with no "partial" state. It is
    therefore a LINE-coverage gap-finder, not a gcov-style branch-coverage tool.
    Use it to find lines that NO test executes; use the static branch/assertion
    audit (cc_tree_repair_and_coverage_report.md C1 §7) for the which-branch-of-an-
    executed-line gaps that no line tool can see. Coverage proves a line RAN; it
    does not prove the test ASSERTED the correct value.

  Install (portable, no admin required):
    The OpenCppCoverage 0.9.9.0 installer is an Inno Setup archive. Extract it with
    innoextract (portable) and copy the `app\` payload to a stable dir:
      innoextract.exe -e -m OpenCppCoverageSetup-x64-0.9.9.0.exe
      copy .\app\*  C:\Users\<you>\tools\OpenCppCoverage\
    (7-Zip cannot open Inno Setup installers; choco/the .exe installer want admin.)

.EXAMPLE
  pwsh tools\coverage\run_coverage.ps1 -Exe ninja_build_rel\composing_tests.exe -OutTag composing
#>
param(
  [string]$Occ         = "C:\Users\vince\tools\OpenCppCoverage\OpenCppCoverage.exe",
  [string]$Repo        = "C:\s\MS",
  [string]$Exe         = "ninja_build_rel\composing_tests.exe",
  [string]$OutTag      = "composing",
  [string]$OutDir      = "C:\s\MS\scratch_artifacts\coverage",
  [string]$Sources     = "src\composing",
  [string]$GtestFilter = ""
)

if (-not (Test-Path $Occ)) { Write-Error "OpenCppCoverage not found at $Occ"; exit 2 }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
Set-Location $Repo

$exeFull = Join-Path $Repo $Exe
$moduleName = [System.IO.Path]::GetFileName($Exe)
$cobertura = Join-Path $OutDir "$OutTag.cobertura.xml"
$html      = Join-Path $OutDir "$OutTag`_html"
$log       = Join-Path $OutDir "$OutTag`_run.txt"

$occArgs = @(
  "--sources", $Sources,
  "--modules", $moduleName,
  "--export_type", "cobertura:$cobertura",
  "--export_type", "html:$html",
  "--quiet",
  "--"
  $exeFull
)
if ($GtestFilter -ne "") { $occArgs += "--gtest_filter=$GtestFilter" }

Write-Output "OpenCppCoverage -> $moduleName (sources=$Sources)"
& $Occ @occArgs > $log 2>&1
$rc = $LASTEXITCODE
Write-Output "exit:$rc  cobertura:$cobertura  html:$html  log:$log"
exit $rc
