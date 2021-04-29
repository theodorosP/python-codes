#write a code to get the lenght of a string

x = list(input("Please give a string to find it's letters: "))
a_dictionary = {}

for i in range(0, len(x)):

    a_dictionary["A_%s" %(i+1)] = x[i]


print(a_dictionary)
