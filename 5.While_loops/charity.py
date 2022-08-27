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
