authorized_users = [
	{
		'name' : 'Sagar Aryal',
		'email' : 'sagararyal@gmail.com',
		'password' : 'sagar'
	},
	{
		'name' : 'Ayush Ban',
		'email' : 'ayushban100@gmail.com'
		'password' : 'ayush'
	}
]


def main():
	email = input('Enter Email: ')
	password = input('Enter Password: ')

	print()

	(user_exits, login_sucess) = check_login(email, password)

	if user_exits == False:
		print




def
	login_sucess = False
	user_exits = False

for user in authorized_users:
	if email == user['email'] and password == user['password']:
		login_sucess = True
		print('User Found')
		print('Name: {}' .format(user['name']))
		print('Email: {}' . format(user['email']))
		break

	elif email == user['email']:
		user_exits = True
print()

if login_sucess == False:
	print('Access Denied')