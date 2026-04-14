@echo off
CALL "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
cd /d c:\s\MS\ninja_build_rel
ninja composing_tests notation_tests MuseScore5.exe batch_analyze
