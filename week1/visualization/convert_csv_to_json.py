import csv
import json
import random
import pprint as pp

nodes = []
edges = []
dummy = {}
size = {}
names = {}
ASN_type_mapping = {}
type_dummy = {}

csvfile = open('2018-07-Domestic Exchange - Index.csv', 'r')
jsonfile = open('domestic.json', 'w')

reader = csv.DictReader(csvfile)

start_size = 5
inc = 1
sname = ''
cate = {}
i = 0
for row in reader:
	sname = row['ASN']


	if sname not in dummy:
		size[row['ASN']] = start_size
		dummy[sname] = sname
		names[row['ASN']] = row['ASN']
	else:
		size[row['ASN']] = float(size[row['ASN']]) + inc
	
	ASN_type_mapping[sname] = row['Type']
	sname = row['ASN-source']


	if sname not in dummy:
		size[row['ASN-source']] = start_size
		dummy[sname] = sname
		names[row['ASN-source']] = row['ASN-source']
	else:
		size[row['ASN-source']] = float(size[row['ASN-source']]) + inc

	ASN_type_mapping[sname] = row['Type']
	my_type = row['Type']


	if my_type not in type_dummy:
		r = lambda: random.randint(0,255)
		color = '#%02X%02X%02X' % (r(),r(),r())
		type_dummy[my_type] = color
		cate[my_type] = i
		i = i + 1

	edge = {}
	edge['sourceID'] = row['ASN-source']
	edge['targetID'] = row['ASN']
	edge['attributes'] = {}
	# edge['size'] = 1
	edge['size'] = float(row['Bandwidth'])/50


	if edge['size'] < 1.0:
		edge['size'] = 0.1
	edges.append(edge)


for i in dummy:
	node = {}
	node['id'] = i
	node['x'] = random.uniform(-1000, 1000)
	node['y'] = random.uniform(-1000, 1000)
	node['size'] = size[i]
	node['attributes'] = {}
	node['label'] = names[i]
	node['color'] = type_dummy[ASN_type_mapping[i]]
	node['category'] = cate[ASN_type_mapping[i]]
	nodes.append(node)

nodes = sorted(nodes, key=lambda k: k['x'], reverse=True) 


data = {}
data['nodes'] = nodes
data['edges'] = edges


json.dump(data, jsonfile)