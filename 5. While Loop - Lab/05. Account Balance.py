number_text = input()

# да се пише ВНОСКА сума
#АКО vnoska < 0 --> Invalid operation!
# STOP --> NoMoreMoney
#Продължи --> vnoska != NoMoreMoney
balance = 0.0
while number_text != "NoMoreMoney":
    amount = float(number_text) # превръщаме str --> float

    if amount < 0:
        print("Invalid operation!")
        break
    balance += amount
    print(f"Increase: {amount:.2f}")
    number_text = input() # за да не се получи безкраен лууп

print(f"Total: {balance:.2f}")