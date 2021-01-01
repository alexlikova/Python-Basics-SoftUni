import math

figure = str(input());

if figure == "square":
    side = float(input());
    result = side * side;
elif figure == "rectangle":
    a = float(input());
    b = float(input());
    result = a * b;
elif figure == "triangle":
    a = float(input());
    h = float(input());
    result = (a * h)/2;
else:
    radius = float(input());
    result = math.pi * radius **2;

print(f"{result: .3f}");
