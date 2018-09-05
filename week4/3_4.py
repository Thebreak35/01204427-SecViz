import csv

dummy = {}
for t in range(0,60):
	if t < 10:
		fname = 'web-anon-20170410030' + str(t) + '.0.txt'
	else:
		fname = 'web-anon-2017041003' + str(t) + '.0.txt'
	f = open(fname, 'r', encoding = "ISO-8859-1")
	for i in f:
		line = []
		line = i.split(' ')
		if line[14] == '80': #line[13] is srcport
			if line[16] != '-' and '158.108.' in line[16]:
				if line[16] not in dummy:
					dummy[line[16]] = 1
				else :
					dummy[line[16]] += 1
o = open('3_4.csv', 'w')
o.write('id,value\n')
for i in dummy:
	text = str(str(i) + ',' + str(dummy[i]))
	o.write(text)
	o.write('\n')

