@echo off
echo ���޸�IE��
 
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f

rem  192.168.1.105:1080 �Ǵ���ip�Ͷ�Ӧ�Ķ˿� 
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "192.168.1.105:1080" /f
  
rem �����ڱ��ص�ַ��ʹ�ô������������������Ṵѡ��
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride /t REG_SZ /d "11.*;68.*;10.*;<local>" /f