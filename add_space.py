while True:
	try:
		x = float(input("Please give a number: "))
	except:
		print("Please try again")
	else:
		break
y = int(x)
#you need for integers, else for float use f
#center
a = "{:^10d}".format(y)

#right aligned
b = "{:10d}".format(y)


#left aligned
c  ="{:<10d}".format(y)

print(a, "\n", b, "\n", c)
