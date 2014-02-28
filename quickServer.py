#!/usr/bin/env python
import SimpleHTTPServer, SocketServer, socket
"""
This will make a quick web host server for the directory it is located
Possibly used for helping a homie with code
Or whatever.
"""
# Get local inet_ip address
def getIP():
    try:
	socket.gethostbyname(socket.gethostname())
    except socket.error as msg:
        print "Not connected to the interwebs"
        sys.exit(-1)
    return socket.gethostbyname(socket.gethostname())

def main():
	PORT = 8000	
	machineIP = getIP()
	print 'This machiens IP is ', machineIP
	print 'To connect, got to web browser and type:',repr('http://'+machineIP+':8000')

	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler	

	httpd = SocketServer.TCPServer(("", PORT), Handler)	

	print "serving at port", PORT
	httpd.serve_forever()

if __name__ == '__main__':
	main()