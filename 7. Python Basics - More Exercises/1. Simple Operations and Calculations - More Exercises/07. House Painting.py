x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
front_back_walls = (2 * (x * x)) - door

window = 1.5 ** 2
side_walls = (2 * (x * y)) - (2 * window)

roof_triangles = 2 * ((x * h) / 2)
roof_rectangles = 2 * x * y

roof_area = roof_triangles + roof_rectangles

green_paint = (front_back_walls + side_walls) / 3.4
red_paint = roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")


