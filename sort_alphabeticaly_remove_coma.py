#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
x = list(input("Please give a setense: ").split())
a = [i.strip().strip(",.") for i in x]
a.sort()
print(a)
