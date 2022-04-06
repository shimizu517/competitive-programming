from typing import List, Tuple


def fractional_knapsack(items: List[Tuple[int]], w):
    _items = sorted(items, key=lambda i: i[0] / i[1], reverse=True)
    result = 0
    c = w
    for _v, _w in _items:
        if _w <= c:
            c -= _w
            result += _v
        else:
            result += (_v / _w) * c
            break
    print(result)


def main():
    n, w = map(int, input().split())
    items = []
    for _ in range(n):
        items.append(tuple(map(int, input().split())))
    fractional_knapsack(items, w)


main()
