n = 0
sum = 0

#calculatte the sum of number of 5 number entered by user

while n < 5:
	value = input('enter the number %s: ' %(n+1))
	sum = sum + float(value)
	n += 1

print ('sum = %.2f' % sum)
