processor = float(input())
video = float(input())
memory = float(input())
memory_count = int(input())
discount = float(input())

total_usd = (processor - processor * discount) + (video - video * discount) + memory * memory_count
total_lv = total_usd * 1.57

print(f"Money needed - {total_lv:.2f} leva.")
