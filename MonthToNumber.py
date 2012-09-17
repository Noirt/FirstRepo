Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> 
>>> 
>>> 
>>> 
>>> def MonthConv():
	monthDict = {"January":1,"February":2,"March":3,"April":4,
		     "May":5,"June":6,"July":7,"August":8,
		     "September":9,"October":10,"November":11,"December":12}
	m = raw_input("Enter month: ")
	print("Month number: %s" % monthDict[m])

	
>>> 
>>> 
>>> MonthConv()
Enter month: October
Month number: 10
>>> MonthConv()
Enter month: May
Month number: 5
>>> 
