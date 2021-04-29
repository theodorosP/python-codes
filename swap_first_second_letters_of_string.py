#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

x1 = list(input("Please give the first string: ")) 
x2 = list(input("Please give the second string: "))

new_x1 = x2[:2] + x1[2:] 

new_x2 = x1[:2] + x2[2:]
a = ""
b = ""
for i in new_x1:
	a += i
for i in new_x2:
	b += i 
c = a + " " + b
print(c)
