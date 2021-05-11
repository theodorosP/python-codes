x = input("Please give a word: ")
if len(x) % 4 ==0:
	y = "".join(reversed(x))
	print(y)
else:
	print(x)	
