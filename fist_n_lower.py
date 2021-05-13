while True:
	try:
		n = int(input("Please give a number: "))
	except:
		print("Please try again")
	else:
		break

l = []
x = input("Give a string: ")
for i in range(0, n):
	a = x[i].lower()
	l.append(a)
print(l)
st = ""
for i in l:
	st = st + i
	
c = st + x[n:]
print(c)
