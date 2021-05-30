# トップダウンの方法でやりたいけどできてない

class Solution:
    ugly_dp = []
    i2, i3, i5 = 0, 0, 0

    def getNthUglyNo(self, n):
        self.ugly_dp = [0] * (n + 1)
        self.ugly_dp[0] = float('inf')
        self.ugly_dp[1] = 1
        return self.ugly(n - 1)

    def ugly(self, n):
        if self.ugly_dp[n] == 0:
            self.ugly_dp[n] = min(
                self.ugly(self.i2 - 1) * 2,
                self.ugly(self.i3 - 1) * 3,
                self.ugly(self.i5 - 1) * 5)

        if self.ugly_dp[n] == self.ugly(n - 1):
            self.i2 += 1
        if self.ugly_dp[n] == self.ugly(n - 1):
            self.i3 += 1
        if self.ugly_dp[n] == self.ugly(n - 1):
            self.i5 += 1

        return self.ugly_dp[n]


n = int(input())
ob = Solution()
print(ob.getNthUglyNo(n))
