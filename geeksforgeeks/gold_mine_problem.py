class Solution:
    mat = []
    dp = []

    def maxGold(self, n, m, M):
        self.mat = M
        self.dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = self.mat[i][0]

        ans = 0
        for i in range(n):
            ans = max(ans, self.get_max(i, m - 1))
        return ans

    def get_max(self, i, j):
        if i < 0 or len(self.mat) <= i:
            return 0
        if self.dp[i][j] >= 0:
            return self.dp[i][j]
        self.dp[i][j] = max(self.get_max(i - 1, j - 1), self.get_max(i, j - 1), self.get_max(i + 1, j - 1)) + \
                        self.mat[i][j]
        return self.dp[i][j]


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(n)]

ob = Solution()
print(ob.maxGold(n, m, mat))
