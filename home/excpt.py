while True:
	a = float(input('Enter the first number: '))
	b = float(input('Enter the second number: '))

	try:
		result = a / b
		print('Result = {}' .format(result))

	except ZeroDivisionError:
		print('Error: Division by error')

	try_again = input('\nTry again (Y/N)? ')

	if try_again.upper() != 'Y':
		break

	print()


print('Goodbye')

