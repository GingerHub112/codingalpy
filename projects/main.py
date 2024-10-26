# Ask input:
msg = input("Type something to turn in uppercase...")

# Algorithm:
print("Processing...")
ret = ""
while (len(msg) > 0):
    ret = ret + msg[0].upper()
    msg = msg[1:len(msg)]

print(ret)