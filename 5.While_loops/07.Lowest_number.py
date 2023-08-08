import sys
min_number = sys.maxsize
otherinput = input()

while otherinput != "Stop":
    number = int(otherinput)
    if number < min_number:
        min_number = number
    otherinput = input()
print(f"{min_number}")
