import collections
print("Input a text in a line.")
#use split to sheperate words with gap
text_list = list(input().split())
#remove ,
a = [elem.strip().strip(',') for elem in text_list]
print(a)


#second way
x = input("Give input: ")
words = [i for i in x.split(",")]
