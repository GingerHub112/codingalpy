print("Welcome to PATTERNS!")
print("------------------------------------")
print("PATTERNS: Star (*) Pyramid")
print("")
stars = ""
rows = int(input("How many rows? "))
for i in range(0, rows):
    stars = stars + "* "
    print(stars)