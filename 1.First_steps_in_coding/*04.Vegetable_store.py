vegets = float(input())
fruits = float(input())
total_weight_vegets = float(input())
total_weight_fruits = float(input())

total_sum = vegets * total_weight_vegets + fruits * total_weight_fruits
total_eu = float(total_sum / 1.94)

print("{:.2f}".format(total_eu))
