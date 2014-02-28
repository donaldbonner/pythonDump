def signal_to_string(self, signalNumber):
    if signalNumber < 0:
        signalNumber = signalNumber * -1

    if signalNumber == signal.SIGINT:
        return "SIGINT - Interrupt (Ctrl+C)"
    elif signalNumber == signal.SIGKILL:
        return "SIGKILL - Killed"
    elif signalNumber == signal.SIGTERM:
        return "SIGTERM - Terminated"
    elif signalNumber == signal.SIGSEGV:
        return "SIGSEGV - Segmentation fault"
    elif signalNumber == signal.SIGHUP:
        return "SIGHUP - Hang up"
    elif signalNumber == signal.SIGBUS:
        return "SIGBUS - Bus error"
    elif signalNumber == signal.SIGILL:
        return "SIGILL - Illegal instruction"
    elif signalNumber == signal.SIGFPE:
        return "SIGFPE - Floating point exception"
    elif signalNumber == signal.SIGPIPE:
        return "SIGPIPE - Broken pipe (write to pipe with no readers)"
    elif signalNumber == signal.SIGABRT:
        return "SIGABRT - Called abort()"
    elif signalNumber == signal.SIGXFSZ:
        return "SIGXFSZ - Process created files that were too big."
    elif signalNumber == signal.SIGXCPU:
        return "SIGXCPU - Process used too much CPU time."
        
    else:
        return "Unknown signal #" + str(signalNumber)