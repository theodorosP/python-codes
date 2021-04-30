#count words in a setense
import collections
print("Input a text in a line.")
#use split to sheperate words with gap
text_list = list(input().split())
a = [elem.strip().strip(',') for elem in text_list]
counts = dict()
for i in a:
	if i in counts:
		counts[i] += 1
	else:
		counts[i] = 1
print(counts)
