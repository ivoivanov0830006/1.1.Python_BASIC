command = input()
total = ""
current_word = ""
word = 0
total_c = 0
total_n = 0
total_o = 0

while command != "End":
    current_letter = command
    end_word = False
    if current_letter == "c":
        if total_c == 0:
            current_letter = current_letter.replace("c", "")
            total_c += 1
    if current_letter == "n":
        if total_n == 0:
            current_letter = current_letter.replace("n", "")
            total_n += 1
    if current_letter == "o":
        if total_o == 0:
            current_letter = current_letter.replace("o", "")
            total_o += 1

    current_word += current_letter
    if total_c == 1 and total_n == 1 and total_o == 1:
        end_word = True
        current_letter = " "
        current_word += current_letter
        total += current_word
        total_c = 0
        total_n = 0
        total_o = 0
        current_word = ""
    command = input()
total_clean = "".join(c for c in total if c.isalpha() or c.isspace())
print(total_clean)

#Напишете програма, която прочита скрито съобщение в поредица от символи. 
#Те се получават по един на ред до получаване на командата "End". Думите се образуват от буквите в реда на четенето им. 
#Символите, които не са латински букви трябва да бъдат игнорирани. Думите скрити в потока са разделени от тайна команда
#от три букви – "c", "o" и "n". При първото получаване на една от тези букви, тя се маркира като срещната, но не се 
#запазва в думата. При всяко следващо нейно срещане се записва нормално в думата. След като са налични и трите символа 
#от командата, се печата думата и интервал " ". Започва се нова дума, която по същия начин чака тайната команда, 
#за да бъде отпечатана.
#Вход
#От конзолата се чете поредица от редове с един символ на всеки до получаване на командата "End".
#Изход
#На конзолата се печата на един ред всяка дума след тайната команда, следвана от интервал.
#Вход                   Изход
#H                      Hello there 
#n
#e
#l
#l
#o
#o
#c
#t
#c
#h
#o
#e
#r
#e
#n
#e
#End
#------------------------------------------------
#o                      Solve me 
#S
#%
#o
#l
#^
#v
#e
#c
#n
#&
#m
#e
#c
#o
#n
#End
