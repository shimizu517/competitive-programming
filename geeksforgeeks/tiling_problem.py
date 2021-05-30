class Solution:
    dp = []

    def numberOfWays(self, n):
        self.dp = [0] * (n + 1)
        return pow(self.ways(n), 1, 10 ** 9 + 7)

    def ways(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.dp[n] != 0:
            return self.dp[n]

        self.dp[n] = self.ways(n - 1) + self.ways(n - 2)

        return self.dp[n]


class Solution2:
    dp = []

    def numberOfWays(self, n):
        self.dp = [0] * (n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.dp[1] = 1
        self.dp[2] = 2
        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 2] + self.dp[i - 1]
        return pow(self.dp[n], 1, 10 ** 9 + 7)


N = int(input())

ob = Solution2()
print(ob.numberOfWays(N))
