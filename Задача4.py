def calculate_cranes(s):
    xy_sum = s / 4
    y = 2 * xy_sum / 3
    x = xy_sum / 3
    return int(x), int(y), int(2 * (x + y))


print(calculate_cranes(6))  # (1, 4, 1)
print(calculate_cranes(24))  # (4, 16, 4)
print(calculate_cranes(60))  # (10, 40, 10)
