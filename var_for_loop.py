#Assign variables x1, x2, x3, x4 by using four loop
set = {}
for i in range(1, 3):
        while True:
                try:
                        set["x%s" %i] = int(input("Give number "+ str(i) + ": "))
                except(ValueError):
                        print("Please try again")
                else:
                        break
