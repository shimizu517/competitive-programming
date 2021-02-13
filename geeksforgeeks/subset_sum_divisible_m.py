"""
方針
    dpにはmによる剰余が存在する場合にTrueが入る
    例）m=4, nums=[1,1]の場合、dp=[False, True, True, False]となる。
    　　これはnums内の数字を全パターン足して(1,2のみ)それぞれmで割った剰余が1と2にしかならないため
solve(self, nums, m)について
    for i in range(n):
        このループはnumsの中でi番目までの数字を使った組合せ(=2**(i+1)-1通り)の足し算の結果のmの剰余をdpに記録するのが目的
    for j in range(n):
        このループはdpを走査してTrueの場合、i番目の数値を足してmで割った余りを作ることができると分かるので、dpに記録するのが目的
"""

class Solution:
    def DivisibleByM(self, nums, m):
        return int(self.solve(nums, m))

    def solve(self, nums, m):
        n = len(nums)
        dp = [False for _ in range(m)]
        for i in range(n):
            if dp[0]:
                return True

            # tempに入れないと、同じnums[i]を2回足してしまう場合が起こりうる
            temp = [False for _ in range(m)]
            for j in range(m):
                if dp[j]:
                    dp[(j + nums[i]) % m] = True

            for j in range(m):
                if temp[j]:
                    dp[j] = True

            dp[nums[i] % m] = True
        return dp[0]


n, m = map(int, input().split())
nums = list(map(int, input().split()))

ob = Solution()
ob.DivisibleByM(nums=nums, m=m)
