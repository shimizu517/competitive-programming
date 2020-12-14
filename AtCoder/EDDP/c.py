from pprint import pprint
from typing import NamedTuple


class Abc(NamedTuple):
    a: int
    b: int
    c: int


def main():
    n = int(input())
    abcs = [Abc(*map(int, input().split())) for _ in range(n)]
    dp = [{"a": 0, "b": 0, "c": 0} for _ in range(n)]
    dp[0]["a"] = abcs[0].a
    dp[0]["b"] = abcs[0].b
    dp[0]["c"] = abcs[0].c
    for i in range(1, n):
        dp[i]["a"] = max(dp[i - 1]["b"] + abcs[i].a, dp[i - 1]["c"] + abcs[i].a)
        dp[i]["b"] = max(dp[i - 1]["a"] + abcs[i].b, dp[i - 1]["c"] + abcs[i].b)
        dp[i]["c"] = max(dp[i - 1]["a"] + abcs[i].c, dp[i - 1]["b"] + abcs[i].c)
    pprint(dp)

    print(max(dp[n - 1].values()))


main()
