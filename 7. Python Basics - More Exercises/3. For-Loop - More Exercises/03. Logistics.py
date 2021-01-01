"""
number_of_loads = int(input())

total_load, bus_load, train_load, truck_load, price, total_price = 0, 0, 0, 0, 0, 0
bus_price = 200
train_price = 120
truck_price = 175

for i in range(number_of_loads):
    load = int(input())

    total_load += load

    if 0 <= load <= 3:
        bus_load += load
        price = bus_price * load
    elif 4 <= load <= 11:
        truck_load += load
        price = truck_price * load
    else:
        train_load += load
        price = train_price * load

    total_price += price

print(f"{total_price / total_load:.2f}\n"
      f"{bus_load / total_load * 100:.2f}%\n"
      f"{truck_load / total_load * 100:.2f}%\n"
      f"{train_load / total_load * 100:.2f}%")
"""

cargo_count = int(input())
cargos_dict = {'all_cargo': 0, 'bus': 0, 'truck': 0, 'train': 0}

for _ in range(cargo_count):
    current_cargo = int(input())
    if current_cargo <= 3:
        cargos_dict['bus'] += current_cargo
    elif 4 <= current_cargo <= 11:
        cargos_dict['truck'] += current_cargo
    else:
        cargos_dict['train'] += current_cargo
    cargos_dict['all_cargo'] += current_cargo

average_price = (cargos_dict['bus'] * 200 + cargos_dict['truck'] * 175 + cargos_dict['train'] * 120) / cargos_dict['all_cargo']

print(f"{average_price:.2f}")
print(f"{cargos_dict['bus'] / cargos_dict['all_cargo'] *  100:.2f}%")
print(f"{cargos_dict['truck'] / cargos_dict['all_cargo'] * 100:.2f}%")
print(f"{cargos_dict['train'] / cargos_dict['all_cargo'] * 100:.2f}%")

