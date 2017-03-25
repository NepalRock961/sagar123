names = ['sagar', 'aryal', 'dhurbe', 'bijay', 'chabi']
print('Names: ')
for name in names:
 	print(' - %s' % name)


my_list = input('enter item: ')
if len(my_list) == 0:
	print('No item on the list')
else:
	print(my_list)