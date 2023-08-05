command = input()
total = ""
current_word = ""

total_c = 0
total_n = 0
total_o = 0

while command != "End":
    current_letter = command
    if current_letter == "c":
        if total_c == 0:
            current_letter = current_letter.replace("c", "")
            total_c += 1
    if current_letter == "n":
        if total_n == 0:
            current_letter = current_letter.replace("n", "")
            total_n += 1
    if current_letter == "o":
        if total_o == 0:
            current_letter = current_letter.replace("o", "")
            total_o += 1

    current_word += current_letter
    if total_c == 1 and total_n == 1 and total_o == 1:
        current_letter = " "
        current_word += current_letter
        total += current_word
        total_c = 0
        total_n = 0
        total_o = 0
        current_word = ""
    command = input()
total_clean = "".join(c for c in total if c.isalpha() or c.isspace())
print(total_clean)
