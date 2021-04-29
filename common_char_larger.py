#write a code that reads an input and gives the most common character and the larger one

import collections
print("Input a text in a line.")
#use split to sheperate words with gap
text_list = list(input().split())
a = [elem.strip().strip(',') for elem in text_list]
print(a)


sc = collections.Counter(a)
common_word = sc.most_common()[0][0]
print(common_word)

max_char = ""
for i in a:
        if len(max_char) < len(i):
                max_char = i
print(max_char)

