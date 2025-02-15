class myClass:
    __private_var = 27
    
    def __private_method(self):
            print("I'm inside myClass!")

    def hello(self):
          print("Private Variable Value: ", myClass.__private_var)

foo = myClass()
foo.hello()