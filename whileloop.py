names = ['Deepak Olee', 'Rajesh Hamal', 'Paras Gautam']
i = 0
total_names = len(names)
print('Users: ')

while i < total_names:
	end = ' and\n' if i == total_names - 2 else '\n'
	print ('* %s' %names[i], end=end)
	i += 1