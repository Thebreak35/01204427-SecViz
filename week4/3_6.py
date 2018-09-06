import json

#Ingress
def find_ip(txt):
	if txt.find('158.108', 0) == 0 or txt.find('10.', 0) == 0 or txt.find('2460:', 0) == 0:
		return True
	else:
		return False

def choose_last(lst):
	n = -1
	for i in lst:
		n += 1
	# if n == 0:
	# 	return '-'
	return str(lst[n])

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
			if line[16] != '-' and find_ip(str(line[11])): #line[11] is dest IP
				# a = line[17].split('.')
				w = choose_last(line[17].split('.'))
				if len(w) <= 10:
					if (w.find('/') == -1 and 
						w.find('?') == -1 and 
						w.find('~') == -1 and 
						w.find('=') == -1 and
						w.find('-') == -1 and
						w.find('(') == -1 and
						w.find(')') == -1):
						if w not in dummy:
							dummy[w] = 1
						else :
							dummy[w] += 1
o = open('3_6.json', 'w', encoding = "ISO-8859-1")
target = []
data = {}
for i in dummy:
	data = {}
	data['value'] = dummy[i]
	data['name'] = i
	target.append(data)
json.dump(target, o)
