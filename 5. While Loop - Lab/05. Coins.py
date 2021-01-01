change = float(input()) # тук е 0,56000000001, трябва да го превърнем в int

counter_coins = 0

change = int(change * 100) # 1,23 лв ще ни стане 123 ст --> ЦЯЛО ЧИСЛО

counter_coins += change // 200 # counter_coins = counter_coins + (change //200) --> 2lv
change = change % 200
counter_coins += change // 100
change = change % 100
counter_coins += change // 50
change = change % 50
counter_coins += change // 20
change = change % 20
counter_coins += change // 10
change = change % 10
counter_coins += change // 5
change = change % 5
counter_coins += change // 2
change = change % 2

if change == 1:
    counter_coins += 1

print(counter_coins)