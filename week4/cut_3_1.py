import json
f = open("web-anon-201704100307.0.txt", 'r', encoding="utf8")
o = open("spam.json", 'w')
dummy = {}
maxnum = -1
username = ''
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
		# print("user : ", line[4], "#number : ", dummy[line[4]])
# data = {}
t = []
target = {}
for d in dummy:
	data = {}
	data['value'] = dummy[d]
	# print(data['value'])
	data['name'] = d
	# print(data['name'])
	t.append(data)
print(t)
target = t
json.dump(target, o)