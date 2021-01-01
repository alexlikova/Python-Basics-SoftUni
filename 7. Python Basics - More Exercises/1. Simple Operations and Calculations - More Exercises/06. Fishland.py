import math

lv_skumria = float(input())
lv_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = float(input())

lv_palamud = lv_skumria * 1.6
lv_safrid = lv_caca * 1.8
lv_midi = 7.50

total_palamud = lv_palamud * kg_palamud
total_safrid = lv_safrid * kg_safrid
total_midi = lv_midi * kg_midi

total_all = total_midi + total_safrid + total_palamud

print(f"{total_all:.2f}")