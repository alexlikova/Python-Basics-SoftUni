width = float(input())
length = float(input())
height = float(input())
percentage_busy_space = float(input())

volume_aquarium = width * length * height

total_l_water = volume_aquarium / 1000
water_busy_space = (percentage_busy_space / 100) * total_l_water
water_free_space = total_l_water - water_busy_space

print(water_free_space)
