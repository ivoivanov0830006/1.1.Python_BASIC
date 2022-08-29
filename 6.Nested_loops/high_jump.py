stick_needed_height = int(input())
stick_current_height = stick_needed_height - 30
training_is_failed = False
is_completed = False
jumps_count = 0
jump_fails = 0
current_height = int(input())

while not is_completed:
    jumps_count += 1
    if current_height > stick_needed_height:
        is_completed = True
        break
    if current_height > stick_current_height:
        jump_fails = 0
        stick_current_height += 5
    else:
        jump_fails += 1
        if jump_fails == 3:
            training_is_failed = True
            break
    if training_is_failed:
        break
    current_height = int(input())
if is_completed:
    print(f"Tihomir succeeded, he jumped over {stick_current_height}cm after {jumps_count} jumps.")
if training_is_failed:
    print(f"Tihomir failed at {stick_current_height}cm after {jumps_count} jumps.")

Българският лекоатлет Тихомир Иванов започва тренировки за предстоящото европейско 
първенство по лека атлетика на закрито в Глазгоу, Шотландия.
Вашата задача е да напишете софтуер, с който Иванов да следи своя прогрес и дали е 
достигнал желаните резултати. В началото програмата получава желаната височина на летвата от Тихомир, 
той започва тренировката си като поставя летвата на височина 30см по-ниско от целта. 
За всяка височина той има право на 3 скока, като за да бъде един скок успешен, 
той трябва да бъде над височината на летвата. При успешен скок (над летвата), 
височината й се вдига с 5 сантиметра. При три неуспешни скока на една и съща височина, 
тренировката приключва с неуспех. При достигане на желаната височина и нейното успешно прескачане, 
тренировката приключва с успех.
Вход
Входът е поредица от цели числа в интервала [100…300]:
На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов 
Изход
На конзолата трябва да се отпечата един ред:
Ако Тихомир не успее да преодолее желаната височина:
"Tihomir failed at {височина на летвата към момента на провала}cm after {брой скокове от началото на тренировката} jumps."
Ако Тихомир успее да преодолее височината:
"Tihomir succeeded, he jumped over {височина на прескочената последно летва}cm after {брой скокове за цялата тренировка} jumps."
Вход                            Изход
231                             Tihomir succeeded, he jumped over 231cm after 7 jumps.
205
212
213
228
229
230
235
------------------------------------------------------------------------------------------
250                             Tihomir failed at 235cm after 8 jumps.
225
224
225
228
231
235
234
235
