v_volume = int(input())
p1 = int(input())
p2 = int(input())
hours_out = float(input())

p1_full = p1 * hours_out
p2_full = p2 * hours_out

total_p1_p2 = p1_full + p2_full

if total_p1_p2 <= v_volume:
    full_pool_percent = total_p1_p2 / v_volume * 100
    p1_full_percent = p1_full / total_p1_p2 * 100
    p2_full_percent = p2_full / total_p1_p2 * 100

    print(f"The pool is {full_pool_percent:.2f}% full. "
          f"Pipe 1: {p1_full_percent:.2f}%. Pipe 2: {p2_full_percent:.2f}%.")
else:
    more_water_pool = abs(total_p1_p2 - v_volume)
    print(f"For {hours_out:.2f} hours the pool overflows with {more_water_pool:.2f} liters.")