import sys

sys.setrecursionlimit(500000)


class Solution:
    # m番目のコインを使ってnを作れる組合せ数
    dp = [[]]

    def count(self, S, m, n):
        self.dp = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            self.dp[i][0] = 1
        return self.get_count(S, m, n)

    def get_count(self, S, m, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if m <= 0 and n >= 1:
            return 0
        self.dp[m][n] = self.count(S, m - 1, n) + self.count(S, m, n - S[m - 1])
        return self.dp[m][n]

    # def get_count(self, S, i, n):
    #     """
    #     配列S内のm番目までのコインのみを使ってnを作る組合せの数を返す
    #     :param S: コインの配列
    #     :param i: 添字i番目までのコインのみを使う。i < len(S)
    #     :param n: コインを使って作る数値
    #     :return: 組み合わせの数
    #     """
    #     if n == 0:
    #         return 1
    #     if n < 0:
    #         return 0
    #     if m <= 0 and n >= 1:
    #         return 0
    #     if self.dp[i][n] >= 0:
    #         return self.dp[i][n]
    #
    #     # m番目のコインを少なくとも1枚使う方法
    #     m_count = self.get_count(S, i, n - S[i])
    #     # m番目のコインを1枚も使わない方法
    #     no_m_count = self.get_count(S, i - 1, n)
    #     self.dp[i][n] = m_count + no_m_count
    #     return self.dp[i][n]


n, m = map(int, input().split())
s = list(map(int, input().split()))

ob = Solution()
print(ob.count(s, m, n))
