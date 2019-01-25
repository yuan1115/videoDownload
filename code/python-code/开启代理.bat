@echo off
echo 【修改IE】
 
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f

rem  192.168.1.105:1080 是代理ip和对应的端口 
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "192.168.1.105:1080" /f
  
rem “对于本地地址不使用代理服务器”这个勾，会勾选上
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride /t REG_SZ /d "11.*;68.*;10.*;<local>" /f