import math

dohod = float(input())
uspeh = float(input())
min_rab_zaplata = float(input())

#income, grade, min_salary = [float(input()) for _ in range(3)]

socialna_stip=0
uspeh_stip = 0

if (dohod < min_rab_zaplata and uspeh >4.50):
    socialna_stip = min_rab_zaplata * 0.35

if (uspeh >= 5.50):
    uspeh_stip = uspeh * 25

if (socialna_stip > uspeh_stip):
    print(f"You get a Social scholarship {math.floor (socialna_stip)} BGN")
elif (socialna_stip < uspeh_stip):
    print(f"You get a scholarship for excellent results {math.floor (uspeh_stip)} BGN")
else:
    print("You cannot get a scholarship!")

