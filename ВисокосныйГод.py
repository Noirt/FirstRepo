Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> 
>>> 
>>> 
>>> def LeapOrNo():
	y = raw_input("Введите год: ")
	y = int(y)
	if y%400 == 0:
		print ("Високосный")
	elif y%100 == 0:
		print("Не високосный")
	elif y%4 == 0:
		print ("Високосный")
	else:
		print("Не високосный")

		
>>> LeapOrNo()
Введите год: 1823
Не високосный
>>> LeapOrNo()
Введите год: 1824
Високосный
>>> LeapOrNo()
Введите год: 1900
Не високосный
>>> LeapOrNo()
Введите год: 2000
Високосный
>>> LeapOrNo()
Введите год: 2004
Високосный
>>> LeapOrNo()
Введите год: 2100
Не високосный
>>> 
