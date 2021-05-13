import string
x = input("Please give a word/setence: ")
a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase)
s = {}
c = {}
for i in x:
	if i not in s:
		s[i] = 1
	else:
		s[i] = s[i] + 1


if len(s) >= 26 and (s[i].islower == True for i in s):
	print("All the AB letters are included")
else:
	print("Not all the letters are included")
