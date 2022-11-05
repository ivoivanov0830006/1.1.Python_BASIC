from math import floor
command = input()
current_most_powerful_word = ""
total_points = 0
current_most_score = 0

while command != "End of words":
    current_word = command
    first_letter = current_word[0]
    total_points = 0
    is_vowed = False
    vowels = "aeiouyAEIOUY"
    for letter in current_word:
        total_points += ord(letter)
        if first_letter in vowels:
            is_vowed = True
    if is_vowed:
        total_points *= len(current_word)
    else:
        total_points /= len(current_word)
        total_points = floor(total_points)
    if total_points >= current_most_score:
        current_most_score = total_points
        current_most_powerful_word = current_word
    command = input()

print(f"The most powerful word is {current_most_powerful_word} - {current_most_score}")


# ------------------------------------- Another Solution -----------------------------
#
# comand = input()
# word = ""
# n_count = 0
# o_count = 0
# c_count = 0
# while comand != "End":
#     letter = ord(comand)
#     cur_letter = 0
#     if 65 <= letter <= 90 or 97 <= letter <= 122:
#         if letter == 110 and n_count < 1:  # n
#             n_count += 1
#         elif letter == 111 and o_count < 1:  # o
#             o_count += 1
#         elif letter == 99 and c_count < 1:  # c
#             c_count += 1
#         else:
#             cur_letter = letter
#             word += chr(cur_letter)
#     if n_count == 1 and c_count == 1 and o_count == 1:
#         print(word, end=" ")
#         n_count = 0
#         c_count = 0
#         o_count = 0
#         word=""
#     comand = input()
