@echo off
CALL "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" > nul 2>&1
IF ERRORLEVEL 1 (
    FOR /f "usebackq tokens=*" %%i in (`"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath`) do SET VS_INSTALL_DIR=%%i
    CALL "%VS_INSTALL_DIR%\VC\Auxiliary\Build\vcvars64.bat" > nul 2>&1
)
cd /d c:\s\MS\ninja_build
ninja composing_analysis
