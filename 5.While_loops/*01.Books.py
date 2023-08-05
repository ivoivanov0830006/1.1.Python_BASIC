wanted_book = input()
current_book = input()
book_count = 0
is_found = False

while current_book != "No More Books":
    if current_book == wanted_book:
        is_found = True
        break
    book_count += 1
    current_book = input()
if is_found:
    print(f"You checked {book_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")

# ------------------------------------- Problem to resolve ------------------------------
#
# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда
# старата библиотека на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете
# програма, в която тя въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга
# или не провери всички книги в библиотеката, програмата трябва да чете всеки път на нов ред името на
# всяка следваща книга (текст), която тя проверява. Книгите в библиотеката са свършили щом получите
# текст "No More Books".
# ⦁	Ако не открие търсената книгата да се отпечата на два реда:
# ⦁	"The book you search is not here!"
# ⦁	"You checked {брой} books."
# ⦁	Ако открие книгата си се отпечатва един ред:
# ⦁	"You checked {брой} books and found it."
# Вход	                            Изход
# Troy                              You checked 2 books and found it.
# Stronger
# Life Style
# Troy
# ----------------------------------------------------------------------
# The Spot                          The book you search is not here!
# Hunger Games                      You checked 4 books.
# Harry Potter
# Torronto
# Spotify
# No More Books
# ------------------------------------------------------------------------
# Bourne                            You checked 10 books and found it.
# True Story
# Forever
# More Space
# The Girl
# Spaceship
# Strongest
# Profit
# Tripple
# Stella
# The Matrix
# Bourne

