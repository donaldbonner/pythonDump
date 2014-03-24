#!/bin/bash
BINPATH=/usr/bin

if [[ "$1" == "install" ]]; then
	chmod a+x ./quickServer

	if [[ ! -e /usr/bin/quickServer ]]; then
		sudo cp quickServer $BINPATH
		echo "copied ./quickServer to $BINPATH/quickServer"
	else
		echo "quickServer already in $BINPATH"
	fi

elif [[ "$1" == "uninstall" ]]; then
	if [[ -e /usr/bin/quickServer ]]; then
		sudo rm /usr/bin/quickServer
		echo "removed $BINPATH/quickServer"
	else
		echo "quickServer not in $BINPATH"
	fi
	
else
	echo 'usage: ./installServer COMMAND'
	echo 'Command options - install or uninstall'
fi