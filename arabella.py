courses = list() 

while True:
	try:
		x = input("Course or EXIT: ")
	except:
		print("Please try again")
	else:
		break


y = "continue"
new = "cont"

while new != "EXIT":
	while y != "EXIT":
		if x != "EXIT":
			try:	
				y = input("Enter a course or type EXIT: ")
			except:
				pass
			courses.append(y)	
		else:
			break

	del courses[-1]

	if len(courses) <= 6:
		for i in range (len(courses)):
			print(i+1 , courses[i])

	while True:
		try:
			num = int(input("Please give the number that you want to drop: "))
		except:
			print("Please give an integer")
		else:
			break

	while True:
		if num-1 not in range (0, len(courses)):
				try:
                        		num = int(input("Please give the course that you want to drop: "))
				except:
					print("Please give an integer")
				else:
					break
		else:
			break
	del courses[num-1]
	print ("Your courses are: ")
	for i in range(0, len(courses)):
		print(i +1, courses[i])

	while True:
		try:	
			new = input("Please give the new course that you want to add, or type EXIT: ")
		except:
			print("Please be careful")
		else:
			break
	courses.append(new)
	courses.append(new)
