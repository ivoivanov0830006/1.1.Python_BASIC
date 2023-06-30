fuel_type = input()
fuel_tank = float(input())
if fuel_type == "Diesel":
    if fuel_tank >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if fuel_tank >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if fuel_tank >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")


# --------------------------- Another Solution ----------------------------
#
# fuel_type = (input())
# volume = int(input())
# if fuel_type == "Diesel" or fuel_type == "Gas" or fuel_type == "Gasoline" :
#     if volume >= 25:
#         print(f"You have enough {(fuel_type).lower()}.")
#     else:
#         print(f"Fill your tank with {(fuel_type).lower()}!")
# else:
#     print("Invalid fuel!")
