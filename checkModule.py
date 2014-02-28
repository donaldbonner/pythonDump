# A small function that checks if a module is installed
# If not installed, prompted if user wants to install
# Module is installed with 'pip'
# Once this is run, import the module in the function that needs it
# Exits program if user does not with to install Module
import sys, subprocess
def exists(module):
	try:
		__import__(module)
		subprocess.call('clear')
	except ImportError:
		print module,'not installed'
		choice = raw_input('Do you want to install %s (y/n)?' % (module))
		if choice.lower() == 'y':
			subprocess.call(['sudo', 'pip', 'install', module])
			subprocess.call('clear')
		else:
			print """To install in the future, type 'sudo pip install %s' """ % (module)
			sys.exit(0)

# If checking module name is all that is desired
def check(module):
	try:
		__import__(module)
		subprocess.call('clear')
	except ImportError:
		print module,'not installed'
		sys.exit(1)