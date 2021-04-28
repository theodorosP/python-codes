#write a code that accepts only letters as input
while True:
        try:
                x = input("Give a string: ")
                if  any(char.isdigit() for char in x):
                        raise NameError
        except(NameError):
                print("Please try again")
        else:
                break
