#!/usr/bin/env python3

# DJ Bonner
# Script to send SMS text via gmail server using python

import smtplib, sys, getpass

#Different host names of providers
#vtext.com - verizon
#tmomail.net - tmobile
#mms.att.net - at&t
# Check for python3
if sys.hexversion < 0x030000F0:
    print("This script requires Python 3")
    sys.exit(1)

#Prompt for phone number
print('What is the receiving phone number?')
number = sys.stdin.readline().strip().replace('-','')
if len(number) != 10:
	print('Invalid phone number')
	sys.exit(1)

#Make sure valid provider
print('What is the receiving phone provider? (at&t, verizon, or tmobile)')
while True:
	prov = sys.stdin.readline().strip()
	if prov == ('at&t' or 'att'):
		host = 'mms.att.net'
		break
	elif prov == 'verizon':
		host = 'vtext.com'
		break
	elif prov == ('tmobile' or 't-mobile'):
		host = 'tmomail.net'
		break
	else:
		print('Not a valid provider.  Re enter provider. (at&t, verizon, or tmobile)')

#Format message to send
textTo = number + '@' + host

#Input message
print('Type a message!')
message = sys.stdin.readline().strip()

#Setup gmail server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

#Enter gmail information
print('Enter your gmail acount')
username = sys.stdin.readline().strip()
password = getpass.getpass("Password for " + username + ":")
server.login(username, password)

#Send the message
server.sendmail(sender, textTo, message)
print('Message sent!')

#Quit the server
server.quit()