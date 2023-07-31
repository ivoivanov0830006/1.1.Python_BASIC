text = input()
sum = 0

for index in range(0, len(text)):
    if text[index] == "a":
        sum = sum + 1
    if text[index] == "e":
        sum = sum + 2
    if text[index] == "i":
        sum = sum + 3
    if text[index] == "o":
        sum = sum + 4
    if text[index] == "u":
        sum = sum + 5
        
print(sum)
