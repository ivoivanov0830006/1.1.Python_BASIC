rent = int(input())
statues = 0.7 * rent
food = 0.85 * statues
sound = 0.5 * food

total = rent + statues + food + sound
print(f"{total:.2f}")
