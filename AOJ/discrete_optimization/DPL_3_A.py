H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(H)]


def solve():
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        dp[i][0] = int(c[i][0] == 0)
    for i in range(W):
        dp[0][i] = int(c[0][i] == 0)

    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = 0 if c[i][j] == 1 else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    max_s = 0
    for row in dp:
        max_s = max(*row, max_s)

    return max_s ** 2


print(solve())
