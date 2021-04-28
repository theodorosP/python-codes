while True:
        try:
                n = int(input("Please give a positive number: "))
                if n <= 0:
                        raise NameError
        except(NameError):
                print("This is negative, please try again...")
        except(ValueError):
                print("This is not an integer but a string, please try again...>
        else:
                break

