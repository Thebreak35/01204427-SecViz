import csv
import json
import random
import pprint as pp

nodes = []
edges = []
dummy = {}
size = {}
color = {}
names = {}

csvfile = open('2018-07-International Exchange - _Index.csv', 'r')
jsonfile = open('inter.json', 'w')

reader = csv.DictReader(csvfile)

start_size = 10
inc = 1.0
sname = ''
for row in reader:
	sname = row['ASN']
	if sname not in dummy:
		size[row['ASN']] = start_size
		dummy[sname] = sname
		names[row['ASN']] = row['ASN']
	else:
		size[row['ASN']] = float(size[row['ASN']]) + inc

	sname = row['ASN-Source']
	if sname not in dummy:
		size[row['ASN-Source']] = start_size
		dummy[sname] = sname
		names[row['ASN-Source']] = row['ASN-Source']
	else:
		size[row['ASN-Source']] = float(size[row['ASN-Source']]) + 0.1

	edge = {}
	edge['sourceID'] = row['ASN-Source']
	edge['targetID'] = row['ASN']
	edge['attributes'] = {}
	edge['size'] = float(row['Bandwidth'])/30
	if edge['size'] < 1.0:
		edge['size'] = 0.1
	edges.append(edge)

r = lambda: random.randint(0,255)

for i in dummy:
	color = '#%02X%02X%02X' % (r(),r(),r())
	node = {}
	node['id'] = i
	node['x'] = random.uniform(-1000, 1000)
	node['y'] = random.uniform(-1000, 1000)
	node['size'] = size[i]
	node['attributes'] = {}
	node['label'] = names[i]
	node['color'] = color
	nodes.append(node)

data = {}
data['nodes'] = nodes
data['edges'] = edges


json.dump(data, jsonfile)