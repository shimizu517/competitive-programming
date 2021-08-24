from typing import List


def multiple_gcd(l: List[int]):
    tmp_gcd = l[0]
    for i in range(1, len(l)):
        tmp_gcd = gcd(x=tmp_gcd, y=l[i])
    return tmp_gcd


def gcd(x, y):
    if y == 0:
        return x
    return gcd(x=y, y=x % y)


def _lcm(x, y):
    return x * y // gcd(x=x, y=y)


def lcm(l):
    _gcd = multiple_gcd(l=l)
    result = l[0]
    for i in range(1, len(l)):
        result = _lcm(x=result, y=l[i])
    return result


def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(lcm(l=l))


main()
