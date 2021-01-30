import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    dp = []

    def nCr(self, n, r):
        self.dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            self.dp[i][0] = 1
            self.dp[i][i] = 1
        return pow(self.getnCr(n, r), 1, 10 ** 9 + 7)

    # 二項係数の公式 C(n,r) = C(n-1,r) + C(n-1,r-1) を使った
    def getnCr(self, n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        if self.dp[n][r] > 0:
            return self.dp[n][r]
        self.dp[n][r] = self.getnCr(n - 1, r) + self.getnCr(n - 1, r - 1)
        return self.dp[n][r]

    # C(n,r) = (n-r+1)/r * C(n,r-1) という漸化式を求めたが失敗
    # def getnCr(self, n, r):
    #     if n < 0 or r < 0 or n < r:
    #         return 0
    #     if self.dp[n][r] > 0:
    #         return self.dp[n][r]
    #     self.dp[n][r] = int(self.getnCr(n, r - 1) * (n - r + 1) / r)
    #     return self.dp[n][r]


n, r = map(int, input().split())
ob = Solution()
print(ob.nCr(n, r))
