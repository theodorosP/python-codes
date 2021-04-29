#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged

x = input("Please give a sting: ")


a = ""
if len(x) < 3:
	print(x)
elif x[len(x) -3] == "i" and x[len(x) -2] == "n" and x[len(x) -1] == "g":
	for i in range(0 , len(x) -3):
		a = a + x[i]
	print(a+"ly")
else:
	a = x +"ing"
	print(a)
