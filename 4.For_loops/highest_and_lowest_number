import sys
count_of_numbers = int(input())
max_number = -sys.maxsize  #za maksmialno golqmo chislo, vavejdame nai-malkoto vazmojno za da sme sigurni che pri
min_number = sys.maxsize   #vavejdaneto na koeto i da e chislo s "-", to shte e po-golqmo i shte vleze kato maksimalno
for numbers in range(count_of_numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:   # dve otdelni proverki sa zashtoto ako parvoto vavedeno chislo i nai-golqmo
        min_number = current_number   # i nai-malko i ako e izpolzvame elif, nqma da se poluchat neshtata
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

# OR ako iskame bez sys.****** SECOND SOLUTION

count_of_numbers = int(input())
current_number = int(input())
max_number = current_number
min_number = current_number
for numbers in range(count_of_numbers):
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

#Напишете програма, която чете n на брой цели числа. 
#Принтирайте най-голямото и най-малкото число сред въведените.
#вход                 изход
#5                    Max number: 304
#10                   Min number: 0
#20
#304
#0
#50
#----------------------------------------
#6                    Max number: 1000
#250                  Min number: 0
#5
#2
#0
#100
#1000
