from typing import NamedTuple


class Item(NamedTuple):
    w: int
    v: int


def main():
    n, w = map(int, input().split())
    items = [Item(*map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - items[i - 1].w < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j - items[i - 1].w] + items[i - 1].v, dp[i - 1][j]
                )
    print(dp[n][w])


main()
