@echo off
setlocal enabledelayedexpansion
title youtube-dl_download_playlist.bat
for /f "tokens=*" %%a in (class.txt) do (
    :GOON
    cd mp4/list/
    for /f "delims=;, tokens=1-4" %%i in ("%%a") do ( 
        if not exist %%j ( md %%j )
        cd %%j
        set /a length = 100
        if "%%l"=="" ( set  itag=137 ) else (set itag=%%l)
        set /a page = %%k/!length!
        set /a yu = %%k%%!length!
        for /l %%a in (1,1,!page!) do (
            set /a start = %%a-1
            set /a start = !start!*!length!
            set /a start = !start!+1
            set /a end = %%a*!length!
            if not exist !start!_!end! ( md !start!_!end! ) 
            cd !start!_!end!
            set /a files = 1 
            for %%n in (*) do ( set /a files = !files!+1 )
            if !files! geq 101 ( 
                echo !start!-!end! is exist downloads
            ) else ( 
                youtube-dl --proxy http://127.0.0.1:1080  --playlist-start  !start! --playlist-end !end! -f !itag! -i -v %%i
            )
            cd ../
        )
        if !yu!==0 ( echo %%i下载完成 ) else ( 
            set /a start = !page!*!length!
            set /a start = !start!+1
            if not exist !start!_%%k ( md !start!_%%k ) 
            cd !start!_%%k
            youtube-dl --proxy http://127.0.0.1:1080  --playlist-start  !start!  -f !itag! -i -v %%i
            cd ../
        )  
        cd ../
    )
    cd ../../
)	
pause