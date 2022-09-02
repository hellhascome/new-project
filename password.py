while True:
	log = input('login: ')
	passw = int(input('password(3 trys): '))
	count = 0

	if log == 'master' or log == 'Master' and passw == 1379:
		print('Welcome Master, come play with your puppets!')
		break
	elif log != 'master' or log != 'Master':
		print('Error, wrong username!')
	elif passw != 1379:
		print('Wrong password!')
		break

