annual_fee_basketball_training = int(input())

basketball_shoes = annual_fee_basketball_training * 0.6
basketball_clothes = basketball_shoes * 0.8
basketball = basketball_clothes / 4
basketball_accessories = basketball / 5

total = basketball_shoes + basketball_clothes + basketball + basketball_accessories + annual_fee_basketball_training

print(f"{total:.2f}")

