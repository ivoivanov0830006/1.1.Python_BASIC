season = input()
group_type = input()
students_count = int(input())
stays_count = int(input())

price = 0
sport = ""

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price = 9.6
    elif group_type == "mixed":
        price = 10
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price = 7.2
    elif group_type == "mixed":
        price = 9.5
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price = 15
    elif group_type == "mixed":
        price = 20
        
if students_count >= 50:
    price = price * 0.5
elif 50 > students_count >= 20:
    price = price * 0.85
elif 20 > students_count >= 10:
    price = price * 0.95
    
total = price * stays_count * students_count

if season == "Winter":
    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"
    elif group_type == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"
    elif group_type == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"
    elif group_type == "mixed":
        sport = "Swimming"
        
print(f"{sport} {total:.2f} lv.")

