set = {}
for i in range(1, 3):
        while True:
                try:
                        set["x%s" %i] = int(input("Give number "+ str(i) + ": "))
                except(ValueError):
                        print("Please try again")
                else:
                        break


while set["x1"] != set["x2"]:
        while True:
                try:
                        set["x1"] = int(input("Give number 1: "))
                        set["x2"] = int(input("Give number 2: "))
                except(ValueError):
                        print("Please try again")
                else:
                        break

