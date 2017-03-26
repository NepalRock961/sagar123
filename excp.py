a = float(input('First Number: '))
b = float(input('Second Number: '))

try:
	result = a / b
	print(result)
except ZeroDivisionError:
	print('Error : Dividon by Zero')

