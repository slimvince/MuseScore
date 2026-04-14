@echo off
SET VSWHERE="C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe"
FOR /f "usebackq tokens=*" %%i in (`%VSWHERE% -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath`) do (
  SET VS_INSTALL_DIR=%%i
)
CALL "%VS_INSTALL_DIR%\VC\Auxiliary\Build\vcvars64.bat" 10.0.26100.0

if not exist c:\s\MS\ninja_build_rel\build.ninja (
    echo Configuring build tree...
    cd /d c:\s\MS\ninja_build_rel
    C:\Qt\Tools\CMake_64\bin\cmake.exe .. -GNinja ^
        -DCMAKE_BUILD_TYPE=Release ^
        -DCMAKE_INSTALL_PREFIX=..\build.install ^
        -DMUSESCORE_BUILD_CONFIGURATION=app ^
        -DMUSE_APP_BUILD_MODE=dev ^
        -DCMAKE_BUILD_NUMBER=12345678 ^
        -DMUSESCORE_REVISION=abc123456 ^
        -DMUE_RUN_LRELEASE=ON ^
        -DMUE_DOWNLOAD_SOUNDFONT=ON ^
        -DMUSE_ENABLE_UNIT_TESTS=ON ^
        -DMUE_BUILD_COMPOSING_TESTS=ON ^
        -DMUE_BUILD_NOTATION_TESTS=ON ^
        -DMUSE_COMPILE_USE_UNITY=ON
    if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%
)

cd /d c:\s\MS\ninja_build_rel
ninja composing_tests notation_tests batch_analyze MuseScore5.exe
