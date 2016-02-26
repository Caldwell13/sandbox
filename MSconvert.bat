@ECHO OFF
ECHO ----------------------------------------------------------------------
ECHO Mike's individual .yep to mzXML script
ECHO This script uses Bruker's CompassXport
ECHO Place a single .d folder on the desktop
ECHO Change the -a argument to match the name
ECHO ----------------------------------------------------------------------

CHDIR "C:\Documents and Settings\Michael Caldwell\Desktop"

"C:\Program Files\Bruker Daltonik\CompassXport\CompassXport.exe" -a "Apo Halotag HPLC Peak 1_51_01_15277.d"
