price_pens = 5.8
price_markers = 7.20
price_detergent = 1.2

number_package_pens = int(input())
number_package_markers = int(input())
l_detergent = float(input())
percentage_discount = int(input())

price = price_pens * number_package_pens + price_markers * number_package_markers + price_detergent * l_detergent
discounted_price = price - (price * (percentage_discount/100))

print(f"{discounted_price:.3f}")

