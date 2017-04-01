def fibo2(n):
	result= []
	a,b = 0,1
	while a < n:
		result.append(a)
		a,b = b, a+b
	return result

f100 = fibo2(2000)
print(f100)