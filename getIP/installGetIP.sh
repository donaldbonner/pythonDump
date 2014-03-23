#!/bin/bash
BINPATH=/usr/local/bin

if [[ "$1" == "install" ]]; then
	chmod a+x ./getip

	if [[ ! -e /usr/local/bin/getip ]]; then
		sudo cp getip $BINPATH
		echo "copied ./getip to $BINPATH/getip"
	else
		echo "getip already in $BINPATH"
	fi

elif [[ "$1" == "uninstall" ]]; then
	if [[ -e /usr/local/bin/getip ]]; then
		sudo rm /usr/local/bin/getip
		echo "removed $BINPATH/getip"
	else
		echo "getip not in $BINPATH"
	fi
	
else
	echo 'usage: ./installServer COMMAND'
	echo 'Command options - install or uninstall'
fi