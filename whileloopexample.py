#list and the for loop

names  = ['Deepak ollee', 'Natbar khatri', 'Nilesh shrestha']
print('Users: ')

for name in names:
	end = ' and\n' if name == names[-2] else '\n'

	print(' - %s' % name, end=end)