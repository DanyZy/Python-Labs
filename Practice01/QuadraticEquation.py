import math


def quadratic_equation(a, b, c):
    if a != 0:
        dis = b ** 2 - 4 * a * c
        if dis > 0:
            x1 = (-b + math.sqrt(dis)) / (2 * a)
            x2 = (-b - math.sqrt(dis)) / (2 * a)
            return x1, x2
        elif dis == 0:
            x3 = -b / (2 * a)
            return x3
        else:
            return None


cases = [((1, 0, -1), (1, -1)), ((1, 0, 2), None), ((1, 0, 0), 0), ((1, 1, -2), (1, -2)), ((2, 4, 0), (0, -2))]
for case in cases:
    a, b, c = case[0]
    res = quadratic_equation(a, b, c)
    print("Expected: {}. Got: {}. Input: {}. Assert: {}".format(case[1], res, case[0], res == case[1]))
