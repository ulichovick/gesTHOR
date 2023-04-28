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

desktopshortcut="[Desktop Entry]\nVersion=0.1.4\nName=gesTHOR\nExec=python3 /opt/gesTHOR/gesTHOR.py\nIcon=/opt/gesTHOR/icon/icon.png\nPath=/opt/gesTHOR/\nTerminal=false\nType=Application\nCatgories=Utility;Application;"

echo -e $desktopshortcut >> /usr/share/applications/gesTHOR.desktop

