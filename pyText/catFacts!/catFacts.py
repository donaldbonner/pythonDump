#!/usr/bin/env python3

# DJ Bonner
# Script to send SMS text via gmail server using python 3

import smtplib, sys, getpass, os

# Check for python3
if sys.hexversion < 0x030000F0:
    print("This script requires Python 3")
    sys.exit(1)

if os.path.isfile('factList'):
    print('Fact list is present!')
else:
    print('Fact list is not in directory')
    sys.exit(1)

with open("factList") as f:
	facts = [line.strip() for line in f]

for things in facts:
	print(things)		

sys.exit(0)

# Prompt for phone number
print('What is the receiving phone number?')
number = sys.stdin.readline().strip().replace('-','')
if len(number) != 10:
	print('Invalid phone number')
	sys.exit(1)

#Make sure valid provider
print('What is the receiving phone provider? (at&t, verizon, or tmobile)')
while True:
	prov = sys.stdin.readline().strip().lower()
	if prov == ('at&t' or 'att'):
		host = 'txt.att.net'
		break
	elif prov == 'verizon':
		host = 'vtext.com'
		break
	elif prov == ('tmobile' or 't-mobile'):
		host = 'tmomail.net'
		break
	else:
		print('Not a valid provider.  Re enter provider. (at&t, verizon, or tmobile)')

# Format message to send
# Different host names of providers:
# 	vtext.com - verizon
# 	tmomail.net - tmobile
# 	mms.att.net - at&t
textTo = number + '@' + host

# Input message
print('Type a message!')
message = sys.stdin.readline().strip()

# Setup gmail server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

# Enter gmail information
print('Enter your gmail acount')
username = sys.stdin.readline().strip()
password = getpass.getpass("Password for " + username + ":")
server.login(username, password)

# Send the message
server.sendmail(username, textTo, message)
print('Message sent!')

# Logout the server
server.quit()
sys.exit(0)