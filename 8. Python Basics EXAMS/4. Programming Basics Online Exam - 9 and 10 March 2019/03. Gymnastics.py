country = input()
device = input()

max_score = 20

rhythmic_gymnastics = {
    "Russia": {"ribbon": {"difficulty": 9.1, "execution": 9.4}, "hoop": {"difficulty": 9.3, "execution": 9.8}, "rope": {"difficulty": 9.6, "execution": 9.0}},
    "Bulgaria": {"ribbon": {"difficulty": 9.6, "execution": 9.4}, "hoop": {"difficulty": 9.55, "execution": 9.75}, "rope": {"difficulty": 9.5, "execution": 9.4}},
    "Italy": {"ribbon": {"difficulty": 9.2, "execution": 9.5}, "hoop": {"difficulty": 9.45, "execution": 9.35}, "rope": {"difficulty": 9.7, "execution": 9.15}}
}

total_sum = sum(rhythmic_gymnastics[country][device].values())
percent_not_enough = ((max_score - total_sum) / max_score) * 100
print(f"The team of {country} get {total_sum:.3f} on {device}.")
print(f"{percent_not_enough:.2f}%")