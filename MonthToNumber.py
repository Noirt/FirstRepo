def MonthConv():
	monthDict = {"January":1,"February":2,"March":3,"April":4,
		     "May":5,"June":6,"July":7,"August":8,
		     "September":9,"October":10,"November":11,"December":12}
	m = raw_input("Enter month name: ")
	m = m[0].upper() + m[1:]
	if monthDict.has_key(m) == True:
		print("Month number: %s" % monthDict[m])
	else:
		print("Error. No such month.")

MonthConv()

