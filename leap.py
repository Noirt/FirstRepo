def LeapOrNo():
	y = raw_input("Enter year: ")
	y = int(y)
	if y%400 == 0:
		print ("Leap")
	elif y%100 == 0:
		print("Not Leap")
	elif y%4 == 0:
		print ("Leap")
	else:
		print("Not Leap")

LeapOrNo()
