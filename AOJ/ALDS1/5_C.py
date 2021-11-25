import math
from typing import Tuple


def print_coordinate(t: Tuple[float, float]):
    print(f'{t[0]} {t[1]}')


def koch(depth: int, l: Tuple[float, float], r: Tuple[float, float]):
    if depth == 0:
        return
    depth -= 1
    p1: Tuple[float, float] = ((2 * l[0] + r[0]) / 3, (2 * l[1] + r[1]) / 3)
    p3: Tuple[float, float] = ((l[0] + 2 * r[0]) / 3, (l[1] + 2 * r[1]) / 3)
    rad = math.radians(60)
    p2: Tuple[float, float] = (
        p1[0] + math.cos(rad) * (p3[0] - p1[0]) - math.sin(rad) * (p3[1] - p1[1]),
        p1[1] + math.sin(rad) * (p3[0] - p1[0]) + math.cos(rad) * (p3[1] - p1[1]),
    )
    koch(depth=depth, l=l, r=p1)
    print_coordinate(p1)
    koch(depth=depth, l=p1, r=p2)
    print_coordinate(p2)
    koch(depth=depth, l=p2, r=p3)
    print_coordinate(p3)
    koch(depth=depth, l=p3, r=r)


def main():
    n = int(input())
    start = (0.00000000, 0.00000000)
    end = (100.00000000, 0.00000000)
    print_coordinate(start)
    koch(depth=n, l=start, r=end)
    print_coordinate(end)


main()
