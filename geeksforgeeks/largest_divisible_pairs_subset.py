class Solution:
    def perfectSum(self, arr, n, sum):
        return self.solve(arr, n, sum)

    def solve(self, arr, n, sum):
        dp = [[[]] * (sum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = [0]

        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j == arr[i - 1]:
                    dp[i][j] = [arr[i - 1]]
                elif j - arr[i - 1] > 0:
                    if len(dp[i - 1][j - arr[i - 1]]) >= 1:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] + [arr[i - 1]]
                else:
                    if len(dp[i - 1][j]) >= 1:
                        dp[i][j].extend(dp[i - 1][j])

        results = [set(dp[i][sum]) for i in range(1,n+1)]
        return len(set(results))


n, sum = map(int, input().split())
arr = list(map(int, input().split()))




#!/usr/bin/env python
# -*- coding: utf-8 -*-
def perfect_sum(l, i, target, sum, lc):
    # when to stop
    if i == len(l):
        return
    if sum + l[i] == target:
        ldone = lc[:]
        ldone.append(l[i])
        print(ldone)
    if sum + l[i] < target:
        l1 = lc[:]
        l1.append(l[i])
        perfect_sum(l, i + 1, target, sum + l[i], l1)
    # We can always skip
    perfect_sum(l, i + 1, target, sum, lc)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    target = 10
    perfect_sum(a, 0, target, 0, [])
    print("Other example")
    a = [2, 3, 5, 6, 8, 10]
    target = 10
    perfect_sum(a, 0, target, 0, [])
    print("One more")
    a = [3, 34, 4, 12, 5, 2]
    target = 9
    perfect_sum(a, 0, target, 0, [])

