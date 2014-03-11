""" make sure input is a number """
def isPosNum(prompt):
	num = raw_input(prompt).replace(' ','')
	while True:
		try:
			int(num)
		except ValueError:
			num = raw_input('Enter an number: ')
			continue
		else:
			break
	while int(num) < 0:
		num = raw_input('a credit card number is not negative, ya dingus:')
	return num
