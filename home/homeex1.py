def main():
	while True:
		radius = input('Enter the radius of circle in meters: ')

		try:
			PI = 3.145
			radius = float(radius)
			area =PI * radius ** 2
			print('the area of circle = %.2f Sq. meters' %area)
		
		except ValueError:
			print('Invalid Input.Please enter the numeric value')


		try_again = input('\n Try Again(Y/N)? ')
		if try_again.upper() != 'Y':
			break
			print()
	print('Good bye')
main()