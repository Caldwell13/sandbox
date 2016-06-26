@ECHO OFF

ECHO ----------------------------------------------------------------------
ECHO. 
ECHO Mike's automated .yep to mzXML script
ECHO This script uses Bruker's CompassXport
ECHO Place .d folders in E:\ (The location of Handshake on this system)
ECHO This script will convert to mzXML and place in E:\
ECHO.
ECHO ----------------------------------------------------------------------

CD /D E:\
FOR /R %%i IN (*.yep) DO "C:\Program Files\Bruker Daltonik\CompassXport\CompassXport.exe" -a %%i
FOR /R %%i IN (*.mzXML) DO MOVE %%i "E:\"