import json
dummy = []
data = []
target = []
for t in range(0,60):
	if t < 10:
		fname = 'web-anon-20170410030' + str(t) + '.0.txt'
		timetxt = '03:0' + str(t) + ' AM'
	else:
		fname = 'web-anon-2017041003' + str(t) + '.0.txt'
		timetxt = '03:' + str(t) + ' AM'
	f = open(fname, 'r', encoding = "ISO-8859-1")
	n = 0
	for i in f:
		line = []
		line = i.split(' ')
		n += 1
	dummy.append(timetxt)
	data.append(n)
target = [dummy, data]	
o = open('3_1.json', 'w', encoding = "ISO-8859-1")
json.dump(target, o)