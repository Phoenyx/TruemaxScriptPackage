@echo off

SET configFile="config.ini"

IF EXIST config.ini.example ECHO You are trying to install this from the script update location, please move install.cmd into your scripts directory on your computer & GOTO pressKey

ECHO This script will install Truemax Scripts automatically for you, please ask your Technical Director or Teacher if you don't know the information asked of you below.

:getDownloadLocation
SET /P downloadLocation=Please enter the scripts download location: 
IF NOT EXIST %downloadLocation%\* ECHO Directory doesn't exist or it's a file. & GOTO getDownloadLocation
IF NOT EXIST %downloadLocation%\Truemax ECHO This folder doesn't seem to contain our scripts. & GOTO getDownloadLocation

robocopy %downloadLocation% . /XF LICENSE .gitignore config.ini* install.cmd /XD .idea /E /NFL /NDL /NJH /NJS

IF EXIST %configFile% del /F %configFile%

CALL :dequote downloadLocation
CALL :dequote projectLocation

ECHO [TruemaxManager]>> %configFile%
ECHO downloadLocation=%downloadLocation%>> %configFile%

ECHO Truemax Scripts installed and will now autoload on Maya restart. Please use the in-built update menu to update the scripts in the future.

GOTO pressKey

:DeQuote
for /f "delims=" %%A in ('ECHO %%%1%%') do set %1=%%~A
goto :eof

:pressKey
PAUSE
goto :eof