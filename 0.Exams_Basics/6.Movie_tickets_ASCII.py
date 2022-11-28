a1 = int(input())
a2 = int(input())
a = input()
n = int(a)
m = int(n / 2)


for symbol_1 in range(a1, a2):
    for symbol_2 in range(1, n):
        for symbol_3 in range(1, m):
            current_letter = chr(symbol_1)
            symbol_4 = symbol_1
            if symbol_1 % 2 != 0 and (symbol_2 + symbol_3 + symbol_4) % 2 != 0:
                print(f"{current_letter}-{symbol_2}{symbol_3}{symbol_4}")
