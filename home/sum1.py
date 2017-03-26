#simple program to calculate sum

sum = 0
n = 0
while n < 5:
	value = input('Enter the number %s:' %(n+1))
	sum = sum + float(value)
	n += 1

print('The sum is %.2f:' %sum)