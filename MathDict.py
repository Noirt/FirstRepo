Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> 
>>> 
>>> def MathDict():
	d = {"pi":3.14159265358979323846264338327950288,
	     "e":2.71828182845904523536028747135266250,
	     "y":0.57721566490153286060651209008240243,
	     "fi":1.61803398874989484820458683436563812,
	     "delta":4.66920160910299067185320382046620161}
	s = raw_input("Enter constant and accuracy: ")
	l = s.split(":")
	c = l[0]
	n = int(l[1])
	print("%s = %s" % (c, round(d[c],n)))

	
>>> MathDict()
Enter constant and accuracy: pi:4
pi = 3.1416
>>> MathDict()
Enter constant and accuracy: e:2
e = 2.72
>>> MathDict()
Enter constant and accuracy: delta:7
delta = 4.6692016
>>> 
