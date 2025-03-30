@echo off
set c1=%CD%
%~d0
cd %~d0%~p0
cd ../resources/decks
for /l %%n in (60,1,100) do (
    type nul > deck%%n.txt
)
cd %c1%