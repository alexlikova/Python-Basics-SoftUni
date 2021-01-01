size_eggs = input().title()
colour_eggs = input().title()
number_of_batches = int(input())

painting_eggs_dict = {
    "Large": {"Red": 16, "Green": 12, "Yellow": 9},
    "Medium": {"Red": 13, "Green": 9, "Yellow": 7},
    "Small": {"Red": 9, "Green": 8, "Yellow": 5}
}
revenue = painting_eggs_dict[size_eggs][colour_eggs] * number_of_batches
manufacturing_costs = revenue * 0.35
profit = revenue - manufacturing_costs

print(f"{profit:.2f} leva.")