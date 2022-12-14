month = input()
stays = int(input())
studio = 0
app = 0

if month == "May" or month == "October":
    studio = 50
    app = 65
    if 7 < stays <= 14:
        studio = studio * 0.95
    elif stays > 14:
        studio = studio * 0.7
        app = app * 0.9
elif month == "June" or month == "September":
    studio = 75.2
    app = 68.7
    if stays > 14:
        studio = studio * 0.8
        app = app * 0.9
elif month == "July" or month == "August":
    studio = 76
    app = 77
    if stays > 14:
        app = app * 0.9
total_studio = studio * stays
total_app = app * stays
print(f"Apartment: {total_app:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")

#Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената
#за целия престой за студио и апартамент. Цените зависят от месеца на престоя:
#      Май и октомври	                Юни и септември	                       Юли и август
#   Студио - 50 лв./нощувка	        Студио - 75.20 лв./нощувка	        Студио - 76 лв./нощувка
#   Апартамент - 65 лв./нощувка	    Апартамент - 68.70 лв./нощувка	    Апартамент - 77 лв./нощувка
#Предлагат се и следните отстъпки:
#⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
#Вход
#Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
#⦁	На първия ред е месецът - May, June, July, August, September или October;
#⦁	На втория ред е броят на нощувките - цяло число.
#Изход
#Да се отпечатат на конзолата 2 реда:
#⦁	На първия ред: "Apartment: {цена за целият престой} lv."
#⦁	На втория ред: "Studio: {цена за целият престой} lv."
#Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
#Вход                       Изход
#May                        Apartment: 877.50 lv.
#15                         Studio: 525.00 lv.
#----------------------------------------------------
#June                       Apartment: 961.80 lv.
#14	                        Studio: 1052.80 lv.
#----------------------------------------------------
#August                     Apartment: 1386.00 lv.
#20                         Studio: 1520.00 lv.
