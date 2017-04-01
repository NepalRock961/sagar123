squares = []
for x in range(20):
	squares.append(x**2)

print(squares)

print('----------------------')


combs = []
for a in [1,2,3]:
	for b in [3,1,4]:
		if a !=b:
			combs.append((a,b))

print(combs)