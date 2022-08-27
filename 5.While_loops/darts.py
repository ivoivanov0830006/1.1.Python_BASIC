starting_points = 301
current_points = starting_points
total_success_shots = 0
total_fail_shots = 0
name = input()
command = input()
is_winning = False
is_retired = False

while command != "Retire":
    section = command
    points = int(input())
    if section == "Single":
        points = points
    elif section == "Double":
        points = points * 2
    elif section == "Triple":
        points = points * 3
    total_success_shots += 1
    previous_points = current_points
    current_points -= points
    if current_points == 0:
        is_winning = True
        break
    elif current_points < 0:
        current_points = previous_points
        total_fail_shots += 1
        total_success_shots -= 1
    command = input()
    if command == "Retire":
        is_retired = True
if is_winning:
    print(f"{name} won the leg with {total_success_shots} shots.")
if is_retired:
    print(f"{name} retired after {total_fail_shots} unsuccessful shots.")

#Вашата задача е да напишете програма, която да изчислява, дали даден играч е успял да спечели лег.
#Първоначално играчът започва с 301 точки. Играчът хвърля стрелата върху таблото, като за всяко улучено поле,
#той получава определен брой точки. Всяко поле има по три сектора: единичен (Single) сектор от който се взимат 
#броят точки от полето. Двоен (Double), от него се взимат удвоените точки от полето и троен (Triple) сектор, 
#точките от който са умножени по 3.
#Получените точки от всеки изстрел се изваждат от началните точки, до достигане на 0.
#Забележка: При изстрел, даващ повече точки от наличните, той се зачита за неуспешен и играчът трябва да 
#хвърля отново, докато не уцели точки равни на оставащите или по-малки, такъв удар се счита за успешен.
#Пример: При налични точки 100, удар даващ повече от 100 точки, неуспешен
#При налични точки 100, удар даващ по-малко или равни на 100 точки, успешен
#Вход 
#Първоначално се чете един ред:
#Името на играча - текст
#След това до получаване на команда "Retire" се четат многократно по два реда:
#Поле – текст ("Single", "Double" или "Triple")
#Точки – цяло число в интервала [0… 100]
#Изход
#Играта приключва при въвеждане на команда "Retire" или при изравняване на началните 301 точки към 0. 
#На конзолата трябва да се напечата един ред:
#Ако играчът е спечелил лега:
#"{името на играча} won the leg with {успешните изстрели} shots."
#Ако играчът се е отказал от играта:
#"{името на играча} retired after {неуспешни изстрели} unsuccessful shots."
#Вход                          Изход
#Stephen Bunting               Stephen Bunting won the leg with 6 shots.
#Triple
#20
#Triple
#20
#Triple
#20
#Triple
#20
#Triple
#20
#Triple
#20
#Double
#7
#Single
#12
#Double
#1
#Single
#1
