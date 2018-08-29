
import csv
import random
import json
from datetime import datetime


csvfile = open('login-20170102-anon.csv', 'r')
jsonfile = open('number_user.json', 'w')
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

for row in reader:
    cs = row['login_session_id']
    print(cs)
    # ts = int(row[1])
    # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

data = {

}

# json.dump(data, jsonfile)
