names = ['Sagar Aryal', 'Dhruba Thapa', 'Ashik Thape']

for (index,value) in enumerate(names):
	print('%d \t %s' %(index,value))



print('------------------------------------------------')
user = {
	'name' : 'Jhon Doe',
	'email' : 'sagararyal96@gmail.com',
	'phone' : '9860392666',
	'adress' : 'Gulmi Charpala'
}

for(key, val) in user.items():
	print(' %s : %s' %(key, val))