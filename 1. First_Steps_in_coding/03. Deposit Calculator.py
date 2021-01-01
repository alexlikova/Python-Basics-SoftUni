deposit = float(input());
srok = int(input());
interestRate = float(input());
interestRate = interestRate / 100;

result = (deposit + srok * (deposit * interestRate)/12);
print(result);