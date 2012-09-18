Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> def add():
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

				
>>> def f_ip():
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

			
>>> 
>>> 
>>> def f_host():
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

			
>>> def main():
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
		else:
			print("Unknown command.")

			
>>> main()
Enter command: add
ip host list:
192.168.2.4 hostunknown
1.1.1.1 first
127.0.0.1 local
77.88.2.4 y
Add new(y/n): y
<ip> <host>: 13.24.35 yr
Wrong format. Try again.
<ip> <host>: 13.24.35.46 yr
Enter command: add
ip host list:
192.168.2.4 hostunknown
1.1.1.1 first
127.0.0.1 local
77.88.2.4 y
13.24.35.46 yr
Add new(y/n): n
Enter command: find ip
Enter ip: 1.1.1.1
1.1.1.1 first
Enter command: find ip
Enter ip: 2.2.2.2
No such ip.
Enter command: find ip
Enter ip: a.s.d.f
Wrong format. Try again.
Enter ip: 1.1.1
Wrong format. Try again.
Enter ip: 1.1.1.1
1.1.1.1 first
Enter command: find host
Enter host: Y
Wrong format. Try again.
Enter host: y
y 77.88.2.4
Enter command: find host
Enter host: yr1
No such host.
Enter command: quit
>>> 
