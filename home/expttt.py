while True:
	try:
		x = int(input('Enter the number'))
		break
		
	except ValueError:
		print('Oops! That was no valid number.Try again..')
