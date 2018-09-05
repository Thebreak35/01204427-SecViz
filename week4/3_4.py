import csv

#Ingress
def find_ip(txt):
	if txt.find('158.108', 0) == 0 or txt.find('10.', 0) == 0 or txt.find('2460:', 0) == 0:
		return True
	else:
		return False

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
		#All http requests
		if line[14] == '80': #line[13] is srcport
			#ingress
			# print(line[11])
			if line[16] != '-' and find_ip(str(line[11])): #line[11] is dest IP
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

