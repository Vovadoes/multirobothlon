import math

# import numpy as np


def distance(a: tuple[float, float], b: tuple[float, float]):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def volume_tetrahedron(x1: float, x2: float, x3: float, x4: float, y1: float, y2: float, y3: float,
                       y4: float, z1: float, z2: float, z3: float, z4: float) -> float:
    a1 = x2 - x1
    a2 = x3 - x1
    a3 = x4 - x1

    b1 = y2 - y1
    b2 = y3 - y1
    b3 = y4 - y1

    c1 = z2 - z1
    c2 = z3 - z1
    c3 = z4 - z1
    # n_array = np.array(
    #     [[a1, b1, c1],
    #      [a2, b2, c2],
    #      [a3, b3, c3]]
    # )
    # n_array = np.array(
    #     [[1, x1, y1, z1],
    #      [1, x2, y2, z2],
    #      [1, x3, y3, z3],
    #      [1, x4, y4, z4]]
    # )
    # v = np.linalg.det(n_array) / 6

    v = (a1 * (b2 * c3 - c2 * b3) - b1 * (a2 * c3 - c2 * a3) + c1 * (a2 * b3 - a3 * b2)) / 6

    return abs(v)


def volume(lst: list[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> tuple[float, float]:
    coords_min_height = min(lst, key=lambda x: x[2])
    min_height = coords_min_height[2]
    print(f"{min_height=}")

    coords_max_height = max(lst, key=lambda x: x[2])
    max_height = coords_max_height[2]
    print(f"{max_height=}")

    coords_medium_height = lst[(3 - lst.index(coords_min_height) - lst.index(coords_max_height))]
    medium_height = coords_medium_height[2]
    print(f"{medium_height=}")

    a = distance(coords_min_height, coords_medium_height)
    b = distance(coords_medium_height, coords_max_height)
    c = distance(coords_max_height, coords_min_height)
    p = (a + b + c) / 2
    s1 = math.sqrt(p * (p - a) * (p - b) * (p - c))
    v1 = s1 * min_height

    print(f"{s1=}")
    print(f"{v1=}")
    del p

    min_height = 0
    medium_height -= min_height
    max_height -= min_height
    coords_min_height = (coords_min_height[0], coords_min_height[1], 0)
    coords_medium_height = (coords_medium_height[0], coords_medium_height[1], medium_height)
    coords_max_height = (coords_max_height[0], coords_max_height[1], max_height)

    x1, y1, z1 = coords_min_height
    x4, y4, z4 = coords_medium_height
    x5, y5, z5 = coords_max_height
    x2, y2, z2 = x4, y4, 0
    x3, y3, z3 = x5, y5, 0

    v2 = volume_tetrahedron(x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4)
    print(f"{v2=}")
    v3 = volume_tetrahedron(x1, x5, x3, x4, y1, y5, y3, y4, z1, z5, z3, z4)
    print(f"{v3=}")

    return s1, v1+v2+v3


print(volume([(0, 0, 3), (0, 4, 4), (3, 0, 5)]))
# print(volume_tetrahedron(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1))
