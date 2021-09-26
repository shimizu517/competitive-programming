from typing import List


def max_profit(l: List[int]) -> int:
    _max = 10 ** 9 * (-1)
    _min = l[0]
    for i in range(1, len(l)):
        _max = max(_max, l[i] - _min)
        _min = min(_min, l[i])
    return _max


def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))
    print(max_profit(l=l))


main()
