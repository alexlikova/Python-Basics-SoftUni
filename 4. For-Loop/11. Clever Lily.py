age = int(input())
machine = float(input())
toy_price = int(input())

money = 0.0
toys = 0

for number in range(1, age + 1):
    if number % 2 ==0: # гледаме позизията дали е четна или нечетна
        money = ((number * 5) - 1) + money # брат и взима по 1 лв от всеки едни четен рожден ден

    else:
        toys += 1 #за всеки нечетен рожден ден по 1 играчка

money_toys = toy_price * toys
total_money = money + money_toys

if (total_money >= machine):
    print(f"Yes! {total_money - machine:.2f}")
else:
    print(f"No! {abs(total_money - machine):.2f}")