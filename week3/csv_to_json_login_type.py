
import csv
import random
import json
from datetime import datetime


csvfile = open('login-20170102-anon.csv.txt', 'r')
jsonfile = open('login_type.json', 'w')
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

set_login_type = {}
for row in reader:
	inp = {}
	inp = row['agent_type']
	if inp not in set_login_type:
		set_login_type[inp] = 1
	else:
		set_login_type[inp] += 1

data = set_login_type
json.dump(data, jsonfile)
