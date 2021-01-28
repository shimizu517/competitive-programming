import sys

sys.setrecursionlimit(10 ** 7)


def findCatalan(n):
    dp = [-1] * (n + 1)
    dp[0] = 1

    def find(n):
        if dp[n] >= 0:
            return dp[n]
        dp[n] = sum([find(i) * find(n - 1 - i) for i in range(n)])
        return dp[n]

    return find(n)


n = int(input())
print(findCatalan(n))
