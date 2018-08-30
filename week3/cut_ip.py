import json
with open('ip_log.json') as f:
	data = json.load(f)

ipv4 = []
ipv6 = []
dual_stack = []
target = []
for i in data:
	line = []
	line = data[i]
	ipv4.append(line['ipv4'])
	ipv6.append(line['ipv6'])
	dual_stack.append(line['dualstack'])
target = [ipv4, ipv6, dual_stack]

with open('ipcount.json', 'w') as o:
	json.dump(target, o)

