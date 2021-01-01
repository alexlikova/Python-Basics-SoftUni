weather = float(input())
state = ""
if 5 <= weather <= 11.9:
    state = "Cold"
elif 12 <= weather <= 14.9:
    state = "Cool"
elif 15 <= weather <= 20.0:
    state = "Mild"
elif 20.1 <= weather <= 25.9:
    state = "Warm"
elif 26.0 <= weather <= 35.0:
    state = "Hot"
else:
    state = "unknown"

print(state)