#!/bin/bash
cp -a . /opt/gesTHOR
cd /opt/gesTHOR
workpath=$PWD
echo "${workpath}"
mainfilepath=/gesTHOR.py
workpath+=$mainfilepath
echo "${workpath}"
chmod +x "${workpath}"
touch /usr/share/applications/gesTHOR.desktop

desktopshortcut="[Desktop Entry]\nVersion=0.1.3\nName=gesTHOR\nExec=python3 /opt/gesTHOR/gesTHOR.py\nPath=/opt/gesTHOR/\nTerminal=false\nType=Application\nCatgories=Utility;Application;"

echo -e $desktopshortcut >> /usr/share/applications/gesTHOR.desktop

