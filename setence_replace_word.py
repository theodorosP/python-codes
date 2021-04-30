#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

x = input("Please give a string: ")
snot = x.find("not")
spoor = x.find("poor")

if spoor > snot and snot > 0 and spoor >0:
	a = x.replace(x[snot:(spoor +4)],"good")
	print(a)
else:
	print(x)
