number1 = int(input())
number2 = int(input())
operator = input()
type_number = ""

if operator == "+":
    total = number1 + number2
    if total % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
    print(f"{number1} {operator} {number2} = {total} - {type_number}")
elif operator == "-":
    total = number1 - number2
    if total % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
    print(f"{number1} {operator} {number2} = {total} - {type_number}")
elif operator == "*":
    total = number1 * number2
    if total % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
    print(f"{number1} {operator} {number2} = {total} - {type_number}")
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        total = number1 / number2
        print(f"{number1} {operator} {number2} = {total:.2f}")
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        total = number1 % number2
        print(f"{number1} {operator} {number2} = {total}")

#Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се извърши 
#дадена математическа операция. Възможните операции са: Събиране(+), Изваждане(-), Умножение(*),  
#Деление(/) и Модулно деление(%). При събиране, изваждане и умножение на конзолата трябва да се 
#отпечатат резултата и дали той е четен или нечетен. При обикновеното деление - резултата. 
#При модулното деление - остатъка. Трябва да се има предвид, че делителят може да е равен на 0 (нула),
#а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.
#Вход
#От конзолата се прочитат 3 реда, въведени от потребителя:
#⦁	N1 - цяло число;
#⦁	N2 - цяло число;
#⦁	Оператор - един символ измежду: "+", "-", "*", "/", "%".
#Изход
#Да се отпечата на конзолата един ред:
#⦁	Ако операцията е събиране, изваждане или умножение:
#⦁	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
#⦁	Ако операцията е деление:
#⦁	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
#⦁	Ако операцията е модулно деление: 
#⦁	"{N1} % {N2} = {остатък}"
#⦁	В случай на деление с 0 (нула): 
#⦁	"Cannot divide {N1} by zero"
#вход                       изход
#10                         10 + 12 = 22 - even
#12
#+
#-----------------------------------------------
#10                         10 - 1 = 9 - odd
#1
#-
#-----------------------------------------------
#10                         Cannot divide 10 by zero
#0
#%
