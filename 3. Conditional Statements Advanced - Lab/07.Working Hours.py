hour = int(input())
day = str(input()).lower()

if day != "sunday" and 10 <= hour <= 18:
    print("open")
else:
    print("closed")