@echo off
setlocal
SET "VSWHERE=C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe"
for /f "usebackq tokens=*" %%i in (`^""%VSWHERE%" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath^"`) do set "VS_INSTALL_DIR=%%i"

if not "%VSCMD_ARG_TGT_ARCH%"=="x64" (
    CALL "%VS_INSTALL_DIR%\VC\Auxiliary\Build\vcvars64.bat" > NUL 2>&1
)

cd /d C:\s\MS\ninja_build_rel
C:\Qt\Tools\Ninja\ninja.exe MuseScoreStudio
