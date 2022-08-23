total_days = int(input())

doctors = 7
total_treated_patients = 0
total_untreated_patients = 0

for days in range(1, total_days + 1):
    untreated_patients = int(input())
    if days % 3 == 0:
        if total_treated_patients < total_untreated_patients:
            doctors += 1
    if doctors >= untreated_patients:
        total_untreated_patients += 0
        total_treated_patients += untreated_patients
    else:
        total_treated_patients += doctors
        total_untreated_patients += untreated_patients - doctors

print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")


#За даден период от време, всеки ден в болницата пристигат пациенти за преглед. 
#Тя разполага първоначално със 7 лекари. Всеки лекар може да преглежда само по един пациент на ден, 
#но понякога има недостиг на лекари, затова останалите пациенти се изпращат в други болници. 
#Всеки трети ден, болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям 
#от броя на прегледаните, се назначава още един лекар. Като назначаването става преди да започне 
#приемът на пациенти за деня. 
#Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
#Вход
#Входът се чете от конзолата и съдържа:
#На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
#На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден. Цяло число в интервала [0…10 000]
#Изход
#Да се отпечатат на конзолата 2 реда :
#На първия ред: "Treated patients: {брой прегледани пациенти}."
#На втория ред: "Untreated patients: {брой непрегледани пациенти}."
#Вход                       Изход
#4                           Treated patients: 23.
#7                           Untreated patients: 21.
#27
#9
#1
#----------------------------------------------------
#6                           Treated patients: 40.
#25                          Untreated patients: 87.
#25
#25
#25
#25
#2
