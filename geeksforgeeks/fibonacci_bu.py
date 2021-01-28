class Solution:
    dp = []

    def nthFibonacci(ob, n):
        ob.dp = [-1] * (n + 1)
        ob.dp[0] = 0
        ob.dp[1] = 1
        for i in range(2, n + 1):
            ob.dp[i] = ob.dp[i - 2] + ob.dp[i - 1]
        return pow(ob.dp[n], 1, 1000000007)


n = int(input())
ob = Solution()
print(ob.nthFibonacci(n))
