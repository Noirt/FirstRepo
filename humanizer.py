Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> 
>>> 
>>> i = 1
>>> d = {}
>>> while i < 21:
	if i==1:
		d[i]="час"
	elif i>1 and i<5:
		d[i]="часа"
	elif i>=5 and i<21:
		d[i]="часов"
	i+=1

	
>>> def humanizer(d, n):
	if isinstance(d, dict):
		print("%s %s" % (n, d[n%20]))
	else:
		print("Error: wrong type. Type must be dict")

		
>>> humanizer(d, 1)
1 час
>>> humanizer(d, 2)
2 часа
>>> humanizer(d, 138)
138 часов
>>> 
>>> c = [1,2,3,4,5,6]
>>> humanizer(c, 2)
Error: wrong type. Type must be dict
>>> v=4
>>> humanizer(v, 2)
Error: wrong type. Type must be dict
>>> 
