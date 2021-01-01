
number = float (input ("Write a number: "))
metric_input = str (input("Input metric: "))
metric_output = str (input("Output metric: "))

if (metric_input== "mm"):
    if (metric_output=="m"):
        calc = number/1000; #m
    else:
        calc = number/10; #cm

elif (metric_input=="cm"):
    if (metric_output=="m"):
        calc = number/100;
    else:
        calc = number*10; #mm  1mm/10 = 0.1sm

elif (metric_input=="m"):
    if (metric_output=="cm"):
        calc = number*100;
    else:
        calc = number*1000;
else:
    print("Enter valid metric - m, cm, mm")

print (f"{calc:.3f}")


#mm = 1000.0;
#sm = 100.0;
#m = 1.0;
"""
number = float (input ("Write a number: "))
metric_input = str (input("Input metric: "))
metric_output = str (input("Output metric: "))


def convertor(metric_input, number):
    if metric_input == "cm":
        number *= 10
    elif metric_input == "m":
        number *= 1000
    if metric_output == "cm":
        number /= 10
    elif metric_output == "m":
        number /= 1000

    return print(f"{number:.3f}")
"""