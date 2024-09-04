# From: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
# Result: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1378928105/?envType=study-plan-v2&envId=top-interview-150
# References
# - https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/


# Iterate prices. Compare current price and the minimum price so far.
# The max diff at ith price is the one when you subtract min price from current price.
# So you can compare all max diff for any prices.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_so_far = prices[0]

        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            result = max(result, prices[i] - min_so_far)

        return result
