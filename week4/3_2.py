import json
f = open('web-anon-201704100300.0.txt', 'r', encoding="utf8")
o = open('3_2.json', 'w')

dummy = {}
maxnum = -1
for i in f:
	line = []
	line = i.split(' ')
	if line[4] != '-':
		if line[4] not in dummy:
			dummy[line[4]] = 1
		else :
			dummy[line[4]] += 1
		if dummy[line[4]] > maxnum:
			maxnum = dummy[line[4]]
			username = line[4]
print(username, " ", maxnum)

for i in f:
	line = []
	line = i.split(' ')
	if line[4] == username:
		