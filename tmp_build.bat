@echo off
CALL "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
echo VCVARS done > C:\s\MS\build_log.txt
cd /d C:\s\MS\ninja_build_rel
echo Starting ninja... >> C:\s\MS\build_log.txt
C:\Qt\Tools\Ninja\ninja.exe batch_analyze >> C:\s\MS\build_log.txt 2>&1
echo Ninja exit: %errorlevel% >> C:\s\MS\build_log.txt
