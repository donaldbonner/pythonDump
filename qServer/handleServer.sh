#!/bin/bash
BINPATH=/usr/local/bin

if [[ "$1" == "install" ]]; then
	chmod a+x ./quickServer

	if [[ ! -e /usr/local/bin/quickServer ]]; then
		sudo cp quickServer $BINPATH
		echo "copied ./quickServer to $BINPATH/quickServer"
	else
		echo "quickServer already in $BINPATH"
	fi

elif [[ "$1" == "uninstall" ]]; then
	if [[ -e /usr/local/bin/quickServer ]]; then
		sudo rm /usr/local/bin/quickServer
		echo "removed $BINPATH/quickServer"
	else
		echo "quickServer not in $BINPATH"
	fi
	
else
	echo 'usage: ./installServer COMMAND'
	echo 'Command options - install or uninstall'
fi