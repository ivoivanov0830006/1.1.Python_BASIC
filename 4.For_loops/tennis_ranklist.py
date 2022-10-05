from math import floor
tours_count = int(input())
start_points = int(input())

win = 2000
final = 1200
semifinal = 720
total_w = 0
total_f = 0
total_sf = 0
count_w = 0

for tour in range(1, tours_count + 1):
    tour_level = input()
    if tour_level == "W":
        total_w += win
        count_w += 1
    elif tour_level == "F":
        total_f += final
    elif tour_level == "SF":
        total_sf += semifinal
total = start_points + total_w + total_f + total_sf
average = floor((total - start_points) / tours_count)
percent_win = (count_w / tours_count) * 100
print(f"Final points: {total}")
print(f"Average points: {average}")
print(f"{percent_win:.2f}%")

# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които
# зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# ⦁	W - ако е победител получава 2000 точки
# ⦁	F - ако е финалист получава 1200 точки
# ⦁	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички
# изиграни турнири и колко процента от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# ⦁	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# ⦁	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# ⦁	Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# ⦁	"Final points: {брой точки след изиграните турнири}"
# ⦁	"Average points: {средно колко точки печели за турнир}"
# ⦁	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се
# форматира до втората цифра след десетичния знак.
# Вход                      Изход
# 5                         Final points: 8040
# 1400                      Average points: 1328 40.00%
# F
# SF
# W
# W
# SF
# -------------------------------------------------------
# 4                         Final points: 6190
# 750                       Average points: 1360
# SF                        50.00%
# W
# SF
# W
