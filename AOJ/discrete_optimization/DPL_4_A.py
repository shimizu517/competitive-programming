import itertools
from collections import defaultdict

def solve(a, b, c, d, v):
    ab = {}
    for a, b in itertools.product(a, b):
        ab[a + b] = ab.get(a + b, 0) + 1
    cd = {}
    for c, d in itertools.product(c, d):
        cd[c + d] = cd.get(c + d, 0) + 1
    result = defaultdict(int)
    for a_plus_b, ab_num in ab.items():
        for c_plus_d, cd_num in cd.items():
            if a_plus_b + c_plus_d == v:
                result[a_plus_b + c_plus_d] += ab_num * cd_num
    return result[v]


def main():
    N, V = map(int, input().split())
    a = [int(item) for item in input().split()]
    b = [int(item) for item in input().split()]
    c = [int(item) for item in input().split()]
    d = [int(item) for item in input().split()]
    print(solve(a, b, c, d, V))


main()
