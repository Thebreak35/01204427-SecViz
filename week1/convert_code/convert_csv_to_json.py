import csv
import json

csvfile = open('2018-07-Domestic Exchange - Index.csv', 'r')
jsonfile = open('2018-07-Domestic Exchange - Index.json', 'w')

fieldnames = ("ASN-source", "ASN", "Name", "Type", "Bandwidth", "Gb/s", "Connectivity Type")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')
