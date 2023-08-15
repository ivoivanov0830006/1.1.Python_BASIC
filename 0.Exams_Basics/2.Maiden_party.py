love_letter = 0.6
wax_rose = 7.2
key_holder = 3.6
painting = 18.2
surprise = 22

needed_money = float(input())
love_letter_count = int(input())
wax_rose_count = int(input())
key_holder_count = int(input())
painting_count = int(input())
surprise_count = int(input())

total_count = love_letter_count + wax_rose_count + key_holder_count + painting_count + surprise_count
total_money = love_letter_count * love_letter + wax_rose_count * wax_rose + \
              key_holder_count * key_holder + painting_count * painting + surprise_count * surprise

if total_count >= 25:
    total_money *= 0.65

final_money = total_money * 0.9
diff = abs(final_money - needed_money)

if final_money >= needed_money:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

