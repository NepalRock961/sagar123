def main():
	
	while True:
		dob = input('Enter your Date of Birth(yyyy-mm-dd): ')
		dob = dob.split('-')
		try:
			dob_timestamp = float(dob[0]) + float(dob[1])/12 + float(dob[2])/365

			today = ['2017', '03', '17']
			today_timestamp = float(today[0]) + float(today[1])/12 + float(today[2])/365


			years = today_timestamp - dob_timestamp
			months = (years - int(years)) * 12
			print('Your age is %d years %d months' % (years, months))

		except ValueError:
			print('Error!Please enter in correct format')
		
		try_again = input('\nTry Again(Y/N)? ')
		if try_again.upper() != 'Y':
			break	

		print()
	
	print('Good bye')

main()