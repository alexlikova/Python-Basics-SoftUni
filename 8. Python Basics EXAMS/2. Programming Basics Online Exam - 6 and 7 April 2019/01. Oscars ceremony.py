rent_hall = int(input())

statuettes = rent_hall * 0.7
catering = statuettes * 0.85
sound_system = catering / 2

total = sound_system + statuettes + catering + rent_hall

print(f"{total:.2f}")