x = input("Please give a word: ")
sum1 = 0
for i in x:
	if i.upper() == i:
		sum1 = sum1 + 1
a = 0
if sum1 >= 2:
	print(x.upper())
else:
	print(x)
