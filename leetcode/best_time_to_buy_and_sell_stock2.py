# From: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
# Result: 
# References
# - https://www.geeksforgeeks.org/stock-buy-sell/?ref=oin_asr1

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.memo(prices)
        return self.accumulate(prices)

    def memo(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        result = 0
        holding = prices[0]
        holding_profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] <= prices[i]:
                # kddp holding
                holding_profit = prices[i] - holding
            else:
                # sell holding stock
                result += holding_profit
                holding = prices[i]
                holding_profit = 0

        result += holding_profit
        return result

    def accumulate(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        result = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                result += prices[i] - prices[i-1]

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit(
        [7,1,5,3,6,4]
    )
    print(result)
