while True:
	a = float(input('First Number: '))
	b = float(input('Second Number'))

	try:
		result = a / b
		print('Result = {}'.format(result))

	except ZeroDivisionError:
		print('Error: Division by zero')

	try_again = input('\nTry Again (Y/N)? ')

	if try_again.upper() != 'Y':
		break
	print()

print('Good Bye!')