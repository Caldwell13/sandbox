#!/bin/bash

echo "-----------------------------------------------------------------------------"
echo " "
echo "MS conversion using headless Windows XP Virtual Box and Bruker CompassXtract"
echo " "
echo "-----------------------------------------------------------------------------"
#check if VB is already on, if not -> start it

if [ $(VBoxManage --nologo list runningvms | wc -l) = 0 ]; then
	VBoxManage --nologo startvm XP1 --type headless 
	echo "Initializing VM..."
	sleep 12s
fi

#run MSIterator script
VBoxManage --nologo guestcontrol XP1 run --exe "C:\\Program Files\\MSIterator\\MSIterator.bat"  --username mike --password mikexx
sleep .5s 

#shut down VB
echo "Conversion complete. Shutting down..."
VBoxManage controlvm XP1 poweroff
