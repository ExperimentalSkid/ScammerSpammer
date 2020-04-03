import requests
import os
import string
import json
import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
i = 1
while True:
	i += 1
	chars = string.ascii_letters + string.digits + '!@#$%^&*()'
	random.seed = (os.urandom(1024))


	url = 'https://www.google.com'

	

	username = randomString() + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	})

	print('sending username ', username, 'and password', password)
