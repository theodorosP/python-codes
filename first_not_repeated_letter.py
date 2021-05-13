x = input("Please give a sting: ")
s = {}
for i in x:
	if i in s:
		s[i] = s[i] + 1
	else:
		s[i] = 1
print(s)
for j in s:
	if s[j] == 1:
		print("Fisrt not repeated:", j)
		break
