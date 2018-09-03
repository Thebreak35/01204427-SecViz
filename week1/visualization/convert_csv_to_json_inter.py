# import csv
# import json
# import random
# from math import exp, expm1, log10

# nodes = []
# edges = []
# dummy = {}
# type_dummy = {}
# ASN_type_mapping = {}
# size = {}
# names = {}
# colors = {}

# csvfile = open('2018-07-International Exchange - _Index.csv', 'r')
# jsonfile = open('inter.json', 'w')

# reader = csv.DictReader(csvfile)

# start_size = 10
# inc = 1.0
# sname = ''
# my_type = ''
# for row in reader:
# 	sname = row['ASN']
# 	if sname not in dummy:
# 		size[row['ASN']] = start_size
# 		dummy[sname] = sname
# 		names[row['ASN']] = row['ASN']
# 	else:
# 		size[row['ASN']] = float(size[row['ASN']]) + inc

# 	ASN_type_mapping[sname] = row['Type']
# 	sname = row['ASN-Source']
# 	if sname not in dummy:
# 		size[row['ASN-Source']] = start_size
# 		dummy[sname] = sname
# 		names[row['ASN-Source']] = row['ASN-Source']
# 	else:
# 		size[row['ASN-Source']] = float(size[row['ASN-Source']]) + 0.1

# 	ASN_type_mapping[sname] = row['Type']
# 	my_type = row['Type']
# 	if my_type not in type_dummy:
# 		r = lambda: random.randint(0,255)
# 		color = '#%02X%02X%02X' % (r(),r(),r())
# 		type_dummy[my_type] = color

# 	edge = {}
# 	edge['sourceID'] = row['ASN-Source']
# 	edge['targetID'] = row['ASN']
# 	edge['attributes'] = {}
# 	edge['size'] = float(row['Bandwidth'])/30
# 	if edge['size'] < 1.0:
# 		edge['size'] = 0.1
# 	edges.append(edge)

# for i in dummy:
# 	node = {}
# 	node['id'] = i
# 	node['x'] = random.uniform(-1000, 1000)
# 	node['y'] = random.uniform(-1000, 1000)
# 	node['size'] = size[i]
# 	node['attributes'] = {}
# 	node['label'] = names[i]
# 	node['color'] = type_dummy[ASN_type_mapping[i]]
# 	nodes.append(node)

# nodes = sorted(nodes, key=lambda k: k['x'], reverse=True)

# data = {}
# data['nodes'] = nodes
# data['edges'] = edges


# json.dump(data, jsonfile)

import csv
import json
import random
from math import exp, expm1, log10

nodes = []
edges = []
dummy = {}
size = {}
names = {}
ASN_type_mapping = {}
ASN_num_mapping = {}
type_dummy = {}
categories = []

csvfile = open('2018-07-International Exchange - _Index.csv', 'r')
jsonfile = open('inter.json', 'w')

reader = csv.DictReader(csvfile)

start_size = 10000
inc = 10000000
sname = ''
i = 0
num = 0
cate = {}
for row in reader:
	sname = row['ASN']
	if sname not in dummy:
		size[row['ASN']] = start_size
		dummy[sname] = sname
		names[row['ASN']] = row['ASN']
		ASN_num_mapping[sname] = num
		num += 1
	else:
		size[row['ASN']] = float(size[row['ASN']]) + inc
	
	ASN_type_mapping[sname] = row['Type']
	sname = row['ASN-source']


	if sname not in dummy:
		size[row['ASN-source']] = start_size
		dummy[sname] = sname
		names[row['ASN-source']] = row['ASN-source']
		ASN_num_mapping[sname] = num
		num += 1
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
		cat = {}
		cat['name'] = ASN_type_mapping[sname]
		cat['keyword'] = {}
		cat['base'] = ASN_type_mapping[sname]
		categories.append(cat)


	edge = {}
	edge['sourceID'] = row['ASN-source']
	edge['targetID'] = row['ASN']
	# edge['size'] = float(row['Bandwidth'])/50
	n = float(row['Bandwidth']) * 100
	edge['size'] = log10(n)
	print("size: ", edge['size'])
	# if edge['size'] < 0.2:
	# 	edge['size'] = 0.2
	edges.append(edge)


for i in dummy:
	node = {}
	node['id'] = i
	node['x'] = random.uniform(-1000, 1000)
	node['y'] = random.uniform(-1000, 1000)
	node['size'] = log10(float(size[i]))
	# node['value'] = 1
	node['attributes'] = {}
	node['label'] = names[i]
	node['color'] = type_dummy[ASN_type_mapping[i]]
	node['category'] = ASN_type_mapping[i]
	nodes.append(node)
	

nodes = sorted(nodes, key=lambda k: k['size'], reverse=True) 


data = {}
# data['type'] = "force"
# data['categories'] = categories
data['nodes'] = nodes
data['edges'] = edges


json.dump(data, jsonfile)