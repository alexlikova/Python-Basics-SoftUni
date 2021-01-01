weather = input().lower()

state = ""
if weather == "sunny":
    state = "It's warm outside!"
else:
    state = "It's cold outside!"

print(state)