import sys

max_number = -sys.maxsize
otherinput = input()

while otherinput != "Stop":
    number = int(otherinput)
    if number > max_number:
        max_number = number
    otherinput = input()
    
print(f"{max_number}")
