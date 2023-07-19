book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time = book_pages / pages_per_hour
time_per_day = time // days

print(time_per_day)
