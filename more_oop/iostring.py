class IOString:
    def input_string(self):
        self.str1 = input("Please enter a string: ").upper()

    def output_string(self):
        print(self.str1)

myStr = IOString()
myStr.input_string()
myStr.output_string()