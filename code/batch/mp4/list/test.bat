@echo off&setlocal enabledelayedexpansion
for %%j in (*.mp4) do (
    set filename=%%~nj
    set filename=!filename:.=_! 
    set filename=!filename: =! 
    if not "!filename!"=="%%~nj" ren "%%j" "!filename!%%~xj" 
)
set /a n=1
for %%i in (*.mp4) do (
   ren "%%i" A!n!.mp4
   set /a n+=1
) 
pause