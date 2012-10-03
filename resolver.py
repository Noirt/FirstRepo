def add():
	d = {}
	f = open('/home/max/Study/Web/work/resolver', 'r')
	stmp = f.read()
	f.close()
	lst = stmp.split("\n")
	import re
	print("ip host list:")
	for c in lst:
		if re.match('([0-9]{1,3}\.){3}([0-9]{1,3}\ ){1}[a-z0-9]+', c) is not None:
			st = c.split(" ")
			ip = st[0]
			host = st[1]
			d[ip] = host
			print(ip+" "+host)
	sc = raw_input("Add new(y/n): ")
	if sc == 'y':
		while True:
			sn = raw_input("<ip> <host>: ")
			if re.match('([0-9]{1,3}\.){3}([0-9]{1,3}\ ){1}[a-z0-9]+', sn) is not None:
				f = open('/home/max/Study/Web/work/resolver', 'w')
				for c in d:
					f.write(c+" "+d[c]+'\n')
				f.write(sn)
				f.close()
				break;
			else:
				print("Wrong format. Try again.")

				
def f_ip():
	d = {}
	f = open('/home/max/Study/Web/work/resolver', 'r')
	stmp = f.read()
	f.close()
	lst = stmp.split("\n")
	import re
	for c in lst:
		if re.match('([0-9]{1,3}\.){3}([0-9]{1,3}\ ){1}[a-z0-9]+', c) is not None:
			st = c.split(" ")
			ip = st[0]
			host = st[1]
			d[ip] = host
	while True:
		sf = raw_input("Enter ip: ")
		if re.match('([0-9]{1,3}\.){3}([0-9]{1,3}){1}[ ]*', sf) is not None:
			if d.has_key(sf):
				print(sf+" "+d[sf])
				break
			else:
				print("No such ip.")
				break
		else:
			print("Wrong format. Try again.")

			
def f_host():
	d = {}
	f = open('/home/max/Study/Web/work/resolver', 'r')
	stmp = f.read()
	f.close()
	lst = stmp.split("\n")
	import re
	for c in lst:
		if re.match('([0-9]{1,3}\.){3}([0-9]{1,3}\ ){1}[a-z0-9]+', c) is not None:
			st = c.split(" ")
			ip = st[0]
			host = st[1]
			d[host] = ip
	while True:
		sf = raw_input("Enter host: ")
		if re.match('[a-z0-9]+[ ]*', sf) is not None:
			if d.has_key(sf):
				print(sf+" "+d[sf])
				break
			else:
				print("No such host.")
				break
		else:
			print("Wrong format. Try again.")

			
def main():
	add()
	while True:
		s = raw_input("Enter command: ")
		if s == "add":
			add()
		elif s == "find host":
			f_host()
		elif s == "find ip":
			f_ip()
		elif s == 'quit':
			break;
		elif s == 'help':
			print('Command list:\nadd\nfind host\nfind ip\nquit\nhelp')
		else:
			print("Unknown command.")

			
main()

