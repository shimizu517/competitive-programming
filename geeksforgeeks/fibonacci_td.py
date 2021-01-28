import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    dp = []

    def nthFibonacci(ob, n):
        ob.dp = [-1] * (n + 1)
        ob.dp[0] = 0
        ob.dp[1] = 1
        return pow(ob.f(n), 1, 1000000007)

    def f(self, n):
        if ob.dp[n] >= 0:
            return ob.dp[n]
        ob.dp[n] = ob.f(n - 1) + ob.f(n - 2)
        return ob.dp[n]


n = int(input())
ob = Solution()
print(ob.nthFibonacci(n))
