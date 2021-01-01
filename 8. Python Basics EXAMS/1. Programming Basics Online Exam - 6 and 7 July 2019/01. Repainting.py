needed_nylon_kvm, needed_paint_l, paint_thinner_l, working_hours = [int(input()) for _ in range(4)]

protective_nylon_lv_kvm = 1.5
paint_lv_l = 14.50
paint_thinner_lv_l = 5

total_price_nylon = (needed_nylon_kvm + 2) * protective_nylon_lv_kvm
total_price_paint = (needed_paint_l * 1.1) * paint_lv_l
total_price_thinner = paint_thinner_l * paint_thinner_lv_l

total_price_material = total_price_nylon + total_price_paint + total_price_thinner + 0.4
price_workers = working_hours * (total_price_material * 0.30)
total = total_price_material + price_workers

print(f"Total expenses: {total:.2f} lv.")
