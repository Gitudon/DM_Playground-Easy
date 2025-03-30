@echo off
set c1=%CD%
%~d0
cd %~d0%~p0
cd ../
uv add -r ./requirements.txt
uv run "./src/dmp.py"
cd %c1%