import requests
from termcolor import colored

users = ['jack', 'admin', 'mike']
passwords = ['fuck', 'iloveu', 'password', 'sketchers']
found = False

for u in users:
	if not found:
		for p in passwords:
			r = requests.get('https://httpbin.org/basic-auth/admin/password', auth=(u, p))
			print('Trying {0}:{1}'.format(u, p))
			if r.status_code == 200:
				print(colored("I'm In", "green"))
				found = True
				break
			else:
				print(colored("Nope", "red"))
	else:
		break
