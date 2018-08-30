
import csv
import random
import json
from datetime import datetime


csvfile = open('login-20170102-anon.csv.txt', 'r')
jsonfile = open('ip_ratio.json', 'w')
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

ipv4_count = 0
ipv6_count = 0
dual_stack_count = 0
for row in reader:
    ipv4 = row['ipv4']
    ipv6 = row['ipv6']
    if ipv4 != '-' and ipv6 != '-':
    	dual_stack_count += 1
    elif ipv4 != '-' and ipv6 == '-':
    	ipv4_count += 1
    elif ipv4 == '-' and ipv6 != '-':
    	ipv6_count += 1

d = {}
d['ipv4'] = ipv4_count
d['ipv6'] = ipv6_count
d['dual stack'] = dual_stack_count

data = {}
data = d
# data['name'] = 'ipv4', 'ipv6', 'dual stack'
# data['value'] = ipv4_count, ipv6_count, dual_stack_count
# datas.append(data)

json.dump(data, jsonfile)
