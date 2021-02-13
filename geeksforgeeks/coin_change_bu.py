class Solution:
    # m番目のコインを使ってnを作れる組合せ数

    def count(self, S, m, n):
        dp = [[0] * m for _ in range(n + 1)]
        for i in range(m):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(m):
                x = dp[i - S[j]][j] if i - S[j] >= 0 else 0
                y = dp[i][j - 1] if j >= 1 else 0
                dp[i][j] = x + y
        return dp[n][m - 1]


n, m = map(int, input().split())
s = list(map(int, input().split()))

ob = Solution()
print(ob.count(s, m, n))
