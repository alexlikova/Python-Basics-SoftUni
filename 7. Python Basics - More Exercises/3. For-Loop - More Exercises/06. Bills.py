from collections import OrderedDict

total_sum = [("Electricity:", 0), ("Water:", 0), ("Internet:", 0), ("Other:", 0)] # creating a list
#it remembers the order how the keys are inserted to the dictionary. If you enter one value with a same key previously
# entered, it will remove the previous value and enter the new value at last.
ordered_total_sum = OrderedDict(total_sum) #save the order in which the data has been entered

water = 20
internet = 15
months = int(input())

for month in range(months):
    electricity = float(input())
    other = (water + internet + electricity) * 1.2

    ordered_total_sum["Electricity:"] += electricity
    ordered_total_sum["Other:"] += other

ordered_total_sum["Water:"] = water * months
ordered_total_sum["Internet:"] = internet * months

values = ordered_total_sum.values() #
total_sum = sum(values) #USE sum() TO SUM THE VALUES IN A DICTIONARY

#total_sum = ordered_total_sum["Electricity:"] + ordered_total_sum["Water:"] + ordered_total_sum["Internet:"] + ordered_total_sum["Other:"]
average_for_all_months = total_sum / months

for key, value in ordered_total_sum.items():
    print(f"{key} {value:.2f} lv")

print(f"Average: {average_for_all_months:.2f} lv")