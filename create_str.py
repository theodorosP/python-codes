#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

x = input("Please give a string: ")
if len(x) <= 2:
        print("Empty sting")
else:
        a = len(x)-1
        b = len(x) 
        str = x[0] + x[1] +x[a-1] + x[b-1]
        print(str)
