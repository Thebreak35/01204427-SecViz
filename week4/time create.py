import json
time = open('time.json', 'w')

txt = "03:00:"
target = []
for i in range(0,60):
	if i < 10:
		t = txt + "0" + str(i)
	else:
		t = txt + str(i)
	target.append(t)
json.dump(target, time)