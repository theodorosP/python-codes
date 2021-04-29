x = list(input("Please give a string: "))
count = 0
for i in range(1, len(x)):
	if x[0] == x[i]:
		count = count + 1
		x[i] = "$"

str1 = ""
for i in x:
	str1 = str1 + i
print(str1)
