import json

with open('login_log.json') as f:
	data = json.load(f)

login = []
logout = []
target = []
for i in data:
	line = []
	line = data[i]
	login.append(line['login'])
	logout.append(line['logout'])
target = [login, logout]

with open('loginlogoutcount.json', 'w') as o:
	json.dump(target, o)