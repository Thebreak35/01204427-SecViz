
import csv
import random
import json
from datetime import datetime


csvfile = open('login-20170102-anon.csv.txt', 'r')
jsonfile = open('user.json', 'w')
reader = csv.DictReader(csvfile,  delimiter=' ', fieldnames=['login_session_id',
'login_timestamp',
'user',
'logout_timestamp',
'mac_address',
'ipv4',
'ipv6',
'agent_ip',
'agent_type',
'via_ip',
'ipv4_byte_in',
'ipv4_byte_out',
'ipv4_pkt_in',
'ipv4_pkt_out',
'ipv6_byte_in',
'ipv6_byte_out',
'ipv6_pkt_in',
'ipv6_pkt_out',
'last_seen_timestamp'
])

data = {}
time = []
dummy_data = {}
dummy_user = {}
for row in reader:
	after = []
	x = str(datetime.fromtimestamp(int(float(row['login_timestamp'])/1000)))
	dummy_user[x] = row['user']
	dummy_data[x] = row['user']

dummy_data = sorted(dummy_data)
for i in dummy_data:
	data[i] = dummy_user[i]
# data = sorted(data)

json.dump(data, jsonfile)
