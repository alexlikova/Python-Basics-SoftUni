hours = int (input ()) # 0...23
min = int (input()) # 0...59

min = min + 15;

if (min > 59):
    hours += 1;
    min -=60;

if (hours >=24):
    hours -=24;

if (0 <= min <=9):
    print(f"{hours}:0{min}")
else:
    print (f"{hours}:{min}")