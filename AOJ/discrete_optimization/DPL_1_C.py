import sys

sys.setrecursionlimit(500000)
MAX = 10 ** 9 + 1


def bu(n, w, vw):
    dp = [[MAX] * (w + 1) for _ in range(n + 1)]
    for i in range(w + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            item_v = vw[i - 1][0]
            item_w = vw[i - 1][1]
            if j < item_w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - item_w] + item_v)

    return dp[n][w]


def td(n, w, vw):
    dp = [[-1] * (w + 1) for _ in range(n + 1)]
    for i in range(w + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    return _rec(n, w, vw, dp)


def _rec(i, j, vw, dp):
    if i <= 0 or j <= 0:
        return 0
    if dp[i][j] >= 0:
        return dp[i][j]
    if j < vw[i - 1][1]:
        dp[i][j] = _rec(i - 1, j, vw, dp)
    else:
        dp[i][j] = max(_rec(i - 1, j, vw, dp), _rec(i, j - vw[i - 1][1], vw, dp) + vw[i - 1][0])
    return dp[i][j]


def main():
    n, w = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(n)]
    # print(bu(n, w, vw))
    print(td(n, w, vw))


main()
