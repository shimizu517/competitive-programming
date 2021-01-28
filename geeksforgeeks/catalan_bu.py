import sys

sys.setrecursionlimit(10 ** 7)


def findCatalan(n):
    dp = [-1] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = sum([dp[j] * dp[i - 1 - j] for j in range(i)])

    return dp[n]


n = int(input())
print(findCatalan(n))
