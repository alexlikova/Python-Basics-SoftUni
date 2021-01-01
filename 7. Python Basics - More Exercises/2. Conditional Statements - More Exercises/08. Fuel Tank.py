type_fuel = input().lower()
fuel_litre = int(input())


if type_fuel == "diesel" or type_fuel == "gas" or type_fuel == "gasoline":
    if fuel_litre >= 25:
        print(f"You have enough {type_fuel}.")
    elif 0 < fuel_litre < 25:
        print(f"Fill your tank with {type_fuel}!")

else:
    print(f"Invalid fuel!")

