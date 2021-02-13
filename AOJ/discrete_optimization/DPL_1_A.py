import sys

sys.setrecursionlimit(500000)
MAX = 500001


# ボトムアップ、2次元DP
def bu_2d(n, m, c):
    dp = [[MAX] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if c[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # minの右の引数をdp[i-1][j - c[i-1]]+1として通らなかった。各1枚しか使えないと誤解していた。
                dp[i][j] = min(dp[i - 1][j], dp[i][j - c[i - 1]] + 1)
    return dp[m][n]


def bu_1d(n, m, c):
    dp = [MAX for _ in range(n + 2)]
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i + c[j] <= n:
                dp[i + c[j]] = min(dp[i + c[j]], dp[i] + 1)
    return dp[n]


def td_2d(n, m, c):
    dp = [[MAX] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0
    return rec(m, n, c, dp)


def rec(i, j, c, dp):
    if j == 0:
        return 0
    if i == 0:
        return MAX
    if dp[i][j] < MAX:
        return dp[i][j]

    if c[i - 1] > j:
        dp[i][j] = rec(i - 1, j, c, dp)
    else:
        dp[i][j] = min(rec(i - 1, j, c, dp), rec(i, j - c[i - 1], c, dp) + 1)
    return dp[i][j]


def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    # print(bu_2d(n, m, c))
    # print(bu_1d(n, m, c))
    print(td_2d(n, m, c))


main()
