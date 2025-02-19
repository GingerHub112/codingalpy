class ioString():
    def __init__(self):
        print("[LOG]: IOString object created!")

    def reverseString(self, str):
        return str[::-1]
    
    def __str__(self):
        return "IOString class for string functions"

io = ioString()
print(io.reverseString("Hello"))