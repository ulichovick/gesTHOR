#!/bin/bash
cp -a . /opt/gesTHOR
cd /opt/gesTHOR
workpath=$PWD
echo "${workpath}"
mainfilepath=/gesTHOR.py
workpath+=$mainfilepath
echo "${workpath}"
chmod +x "${workpath}"
touch /usr/share/applications/GesTHOR.desktop

desktopshortcut="[Desktop Entry] \n
Version=0.1.1 \n
Name=Fuck \n
Comment=Un pequeño instalador/desinstalador de paquetes \n
Exec=sudo python /opt/gesTHOR/gesTHOR.py \n
Path=/opt/gesTHOR/ \n
Terminal=false \n
Type=Application \n
Categories=Utility;Application; \n "

echo -e $desktopshortcut >> /usr/share/applications/GesTHOR.desktop

