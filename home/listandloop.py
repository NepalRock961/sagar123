names = ['helllo', 'its', 'me', 'sagar', 'aryal', '!']
i = 0
total_names = len(names)
print('User: ')

while i < total_names:
	end = ' and\n' if i == total_names - 2 else '\n'
	print('* %s' % names[i], end=end)
	i += 1