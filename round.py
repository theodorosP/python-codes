while True:
	try:
		x = float(input("Please give a number: "))
	except:
		print("Plese try again.")
	else:
		break
#the number 2 represents the number of digits after the coma
a = "{:.2f}".format(x)

#the number 2 represents the number of digits after the coma
b = "{:.2%}".format(x)
print(a, b)
