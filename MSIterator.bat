@ECHO OFF
ECHO ----------------------------------------------------------------------
ECHO Mike's automated .yep to mzXML script
ECHO This script uses Bruker's CompassXport
ECHO Place .d folders in C:\dfiles
ECHO This script will convert to mzXML and place on the desktop
ECHO ----------------------------------------------------------------------

CHDIR "C:\dfiles"
FOR /R %%i IN (*.yep) DO "C:\Program Files\Bruker Daltonik\CompassXport\CompassXport.exe" -a %%i
FOR /R %%i IN (*.mzXML) DO MOVE %%i "C:\Documents and Settings\Michael Caldwell\Desktop"