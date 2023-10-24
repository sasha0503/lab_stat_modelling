import math
import random

"""find area between curves by random sampling"""


def get_area(functions, x_min, x_max, y_min, y_max, n):
    """
    :param functions: list of functions. Input x, y and return boolean
    :param x_min: minimum x
    :param x_max: maximum x
    :param y_min: minimum y
    :param y_max: maximum y
    :param n: number of samples
    :return: area
    """
    area = 0
    for i in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        for function in functions:
            if not function(x, y):
                break
        else:
            area += 1
    return area / n * (x_max - x_min) * (y_max - y_min)


def get_volume(functions, x_min, x_max, y_min, y_max, z_min, z_max, n):
    volume = 0
    for i in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        z = random.uniform(z_min, z_max)
        for function in functions:
            if not function(x, y, z):
                break
        else:
            volume += 1

    return volume / n * (x_max - x_min) * (y_max - y_min) * (z_max - z_min)


def paraboloid(x, y, z):
    return x ** 2 + y ** 2 <= z


def f1(x, y):
    return (-1) * x < y < x


def f2(x, y):
    return 2 * x <= y ** 2 + x ** 2 <= 4 * x


def heart_func(x, y):
    return x ** 2 + (y - math.sqrt(abs(x))) ** 2 - 1 < 0


def curved_rhombus_func(x, y):
    return abs(x) ** (2 / 3) + abs(y) ** (2 / 3) <= 1


if __name__ == '__main__':
    fig_1_area = get_area([f1, f2], 0, 4, -2, 2, 100000)
    heart_area = get_area([heart_func], -1, 1, -1, 2, 100000)
    rhombus_area = get_area([curved_rhombus_func], -1, 1, -1, 1, 100000)

    print(f"fig_1_area: {fig_1_area}")
    print(f"heart_area: {heart_area}")
    print(f"rhombus_area: {rhombus_area}")

    paraboloid_volume = get_volume([paraboloid], -1, 1, -1, 1, 0, 1, 100000)
    print(f"paraboloid_volume: {paraboloid_volume}")
