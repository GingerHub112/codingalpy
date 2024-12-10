rows = int(input("How many rows? "))
subtract = 0
star_template = ""
times = 1

for i in range(1, rows + 1):
    subtract = abs(i - rows)
    for j in range(0, subtract):
        star_template = star_template + "* "
        star_template = star_template + "  "
    print(star_template)
    star_template = ""