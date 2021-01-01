target_steps = 10000

goal_reached = False
total_steps = 0
command = input()
while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= target_steps:
        goal_reached = True
        break
    command = input()

if command == "Going home":
    last_steps = int(input())
    total_steps += last_steps
    if total_steps >= target_steps:
        goal_reached = True

difference = abs(total_steps - target_steps)
if goal_reached:
    print(f"Goal reached! Good job!\n{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
