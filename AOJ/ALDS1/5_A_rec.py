def solve(i, a, m, n, dp):
    if m == 0:
        return True
    if i >= n or m < 0:
        return False
    if dp[i][m] is not None:
        return dp[i][m]
    dp[i][m] = solve(i + 1, a, m, n, dp) or solve(i + 1, a, m - a[i], n, dp)

    return dp[i][m]


def main():
    n = int(input())
    a = list(map(int, input().split()))
    _ = int(input())
    m = list(map(int, input().split()))
    for _m in m:
        dp = [[None] * 2000 for _ in range(n)]
        print('yes' if solve(0, a, _m, n, dp) else 'no')


main()


# ↓なにがいかんか分からん
def solve_rec(a, m, i, n, dp):
    if m == 0:
        return True
    if i >= n or m < 0:
        return False
    if dp[m][i] is not None:
        return dp[m][i]
    dp[m][i] = solve(a, m, i + 1, n, dp) or solve(a, m - a[i], i + 1, n, dp)

    return dp[m][i]
