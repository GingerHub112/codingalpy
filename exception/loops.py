valid = False
while(not valid):
    try:
        n = int(input("Please enter a number: "))
        while (n%2==0):
            print("BYE BYE!")
        valid = True
    except KeyboardInterrupt:
        print("Don't press Ctrl-C in Python programs. Understood?")
    except EOFError:
        print("Don't press Ctrl-C in Python programs. Understood?")
    except ValueError:
        print("Specifically, a integer number!")