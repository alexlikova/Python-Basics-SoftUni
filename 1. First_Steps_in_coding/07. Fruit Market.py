strawberry_price = float(input())
kg_banana = float(input())
kg_orange = float(input())
kg_raspberry = float(input())
kg_strawberry = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2

total_price_strawberry = strawberry_price * kg_strawberry
total_price_raspberry = raspberry_price * kg_raspberry
total_price_orange = orange_price * kg_orange
total_price_banana = banana_price * kg_banana

total_amount = total_price_strawberry + total_price_banana + total_price_raspberry + total_price_orange

print(total_amount)