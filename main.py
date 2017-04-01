import test

def main():
	n = int(input('enter a number'))

	series = test.fibo(n)
	print('Series upto {}: \n {}'.format(n,series))
	print('Factorial of {}: {}'.format(n,test.factorial(n)))
main()