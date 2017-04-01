def cheeseshop(kind, *arguments, **keywords):
	print('-- Do you have any', kind, '?')
	print('--hello how are you man',kind)

	for arg in arguments:
		print(arg)
	print('-' * 40)
	for kw in keywords:
		print(kw,':',keywords[kw])

cheeseshop('Limburger','Its is very runny','its is very bad',

	shop = 'Sagar aryal',
	client= 'Dhruba Thapa',
	skecth = 'Hello')