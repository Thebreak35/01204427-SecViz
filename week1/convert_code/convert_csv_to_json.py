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

csvfile = open('2018-07-Domestic Exchange - Index.csv', 'r')
jsonfile = open('domestic.json', 'w')

reader = csv.DictReader(csvfile)

start_size = 10
sname = ''
for row in reader:
	sname = row['ASN']
	if sname not in dummy:
		size[row['ASN']] = start_size
		dummy[sname] = sname
		names[row['ASN']] = row['Name']
	else:
		size[row['ASN']] = int(size[row['ASN']]) + start_size
	edge = {}
	edge['sourceID'] = row['ASN-source']
	edge['targetID'] = row['ASN']
	edge['attributes'] = {}
	edge['size'] = 1
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