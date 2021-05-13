while True:
	try:
		x = float(input("Please give a number: "))
	except:
		print("Plese try again.")
	else:
		break

a = "{:.2f}".format(x)
print(a)
