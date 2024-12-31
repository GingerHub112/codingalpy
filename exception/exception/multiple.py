try:
    num1, num2 = eval(input("Enter two numbers separated by commas "))
    r = num1 / num2
except ZeroDivisionError:
    print("You can't divide by zero!")
except SyntaxError:
    print("The syntax is incorrect")
except KeyboardInterrupt:
    print("You can't use Ctrl+C in Python as [COPY], it force-quits the program")
except:
    print("The error handling system coudn't detect the error, but there was an unknown error")
else:
    print("The error handling system coudn't detect any errors, HOORAY!")
    print(r)
finally:
    print("THE END!")