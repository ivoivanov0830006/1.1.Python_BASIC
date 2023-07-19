pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())

price_pens = 5.8
price_markers = 7.2
price_cleaner = 1.2

total_pens = price_pens * pens
total_markers = price_markers * markers
total_cleaner = price_cleaner * cleaner
total = total_pens + total_markers + total_cleaner
total_with_discount = total - total * (discount / 100)

print(total_with_discount)
