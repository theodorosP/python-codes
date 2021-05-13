while True:
	try:
		x = float(input("Please give a decimal number: "))
	except:
		print("Please try again")
	else:
		break
a = x - int(x)
while a == 0 :
	print("This is float, please try again : ")
	while True:
		try:
			x = float(input("Please give a DECIMAL: "))
		except:
			print("Please be careful. \n Please try again..")
		else:
			break
	a = x - int(x)
	
