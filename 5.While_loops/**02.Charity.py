needed_money = int(input())
command = input()
total = 0
total_cash = 0
total_card = 0
cash_count = 0
card_count = 0
transaction_count = 0
is_failed = False
is_successful = False

while command != "End":
    current_transaction = int(command)
    transaction_count += 1
    if command == "End":
        is_failed = True
        break
    if transaction_count % 2 != 0 and current_transaction <= 100:
        cash_count += 1
        total_cash += current_transaction
        print("Product sold!")
    elif transaction_count % 2 == 0 and current_transaction >= 10:
        card_count += 1
        total_card += current_transaction
        print("Product sold!")
    else:
        print("Error in transaction!")
    total = total_card + total_cash
    if total >= needed_money:
        is_successful = True
        break
    command = input()

if is_failed or total < needed_money:
    print("Failed to collect required money for charity.")
elif is_successful:
    print(f"Average CS: {total_cash / cash_count:.2f}")
    print(f"Average CC: {total_card / card_count:.2f}")


# На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане
# с карта. Установени са следните правила за заплащане:
# Ако продуктът надвишава 100лв., за него не може да се плати в брой
# Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
#   Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
#   На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства: 
#   цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
#   При успешна транзакция: "Product sold!"
#   При неуспешна транзакция: "Error in transaction!"
# Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да 
# приключи и на конзолата да се изпишат два реда:
#   "Average CS: {средно плащане в кеш на човек}"
#   "Average CC: {средно плащане с карта на човек}" 
# Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# При получаване на команда "End", да се изпише един ред:
#   "Failed to collect required money for charity."
# Вход	                                Изход
# 500                                   Error in transaction!
# 120                                   Error in transaction!
# 8                                     Product sold!
# 63                                    Product sold!
# 256                                   Product sold!
# 78                                    Product sold!
# 317                                   Average CS: 70.50
# 	                                    Average CC: 286.50
# ---------------------------------------------------------------
# 600                                   Product sold!
# 86                                    Product sold!
# 150                                   Product sold!
# 98                                    Product sold!
# 227                                   Failed to collect required money for charity.
# End
