price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = float(input())
kg_fruits = float(input())

total_vegetables = price_kg_vegetables * kg_vegetables
total_fruits = price_kg_fruits * kg_fruits

total_price = (total_vegetables + total_fruits) / 1.94

print(f"{total_price:.2f}")