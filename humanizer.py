def humanizer(d, n):
	if isinstance(d, dict):
		i = 0
		while i < 21:
			if i==1:
				d[i]='chas'
			elif i>1 and i<5:
				d[i]='chasa'
			elif (i>=5 and i<21) or (i == 0):
				d[i]='chasov'
			i+=1
		print("%s %s" % (n, d[n%20]))
	else:
		print("Error: wrong type. Type must be dict")

import re
d = {}
s = ""
while True:
	s = raw_input('(q - quit) Enter number: ')
	if re.match('[0-9]+', s) is not None:
		n = int(s)
		humanizer(d, n)
	elif s=='q': break; 
	else: print('Try again.')

