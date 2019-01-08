@echo off
title 按视频链接下载.bat

for /f "tokens=2 delims==" %%a in ('wmic path win32_operatingsystem get LocalDateTime /value') do (
  set t=%%a
)
set Today=%t:~0,4%-%t:~4,2%-%t:~6,2%

for /f "delims=*" %%i in (%~dp0/vList.txt) do (
   you-get -s 127.0.0.1:1080 --debug --itag=137 -o mp4/link/%Today% %%i
)
pause