days_tournament = int(input())

total_money = 0
total_wins = 0
total_lose = 0
command = input()

for day in range(1, days_tournament + 1):
    money = 0
    count_win = 0
    count_lose = 0
    while command != "Finish":
        sport = command
        result = input()

        if result == "win":
            money += 20
            count_win += 1
            total_wins += 1
        else:
            money += 0
            count_lose += 1
            total_lose += 1
        command = input()

    if count_win > count_lose:
        money *= 1.1
    total_money += money
    count_win = 0
    count_lose = 0
    if command == "Finish" and day != days_tournament:
        command = input()
    else:
        break

if total_wins > total_lose:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")


"""
days = int(input())
all_money = 0
current_money = 0
current_win_games = 0
current_lost_games = 0
win_games = 0
lost_games = 0

for _ in range(0, days ):
     
   while True:
      game = input()

      if game == 'Finish':
         if current_win_games > current_lost_games:
             current_money = current_money * 1.10
             all_money += current_money
         else:    
             all_money += current_money

         current_money = 0
         current_win_games = 0
         current_lost_games = 0
         break
        
      win_or_lose = input()
       
      if  win_or_lose  == 'win':
        current_money += 20
        current_win_games += 1
        win_games += 1
      else:
         current_lost_games += 1
         lost_games += 1

if win_games > lost_games:
  print(f'You won the tournament! Total raised money: {(all_money * 1.20):.2f}')
else:  
   print(f'You lost the tournament! Total raised money: {all_money:.2f}')
"""