@ECHO OFF

PUSHD "%~dp0"

python can_i_use.py ..\data\can_i_use.json ..\can_i_use.md

POPD

PAUSE
EXIT 0
