wanted_height = int(input())

successful_jump = 0
unsuccessful_jump = 0
moving = 5
total_jumps = 0
start_height = wanted_height - 30

for current_height in range(start_height, wanted_height + 1, 5):
    for i in range(1, 4):
        actual_height = int(input())
        total_jumps += 1
        if current_height < actual_height:
            successful_jump += 1
            unsuccessful_jump = 0
            break
        else:
            unsuccessful_jump += 1

    if unsuccessful_jump == 3:
        print(f"Tihomir failed at {actual_height}cm after {total_jumps} jumps.")
        exit()
print(f"Tihomir succeeded, he jumped over {wanted_height}cm after {total_jumps} jumps.")

"""
target = int(input())
current = target - 30
count, fall = 0, 0

while current <= target:
      count += 1
      jump = int(input())

      if current < jump:
        current += 5
        fall = 0
      else:
         fall += 1

      if fall > 2:
            print(f'Tihomir failed at {current}cm after {count} jumps.')
            exit()

print(f'Tihomir succeeded, he jumped over {target}cm after {count} jumps.')
"""