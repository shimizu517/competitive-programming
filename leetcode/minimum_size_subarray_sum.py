# From https://leetcode.com/problems/minimum-size-subarray-sum
# Result: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1336098660/?envType=study-plan-v2&envId=top-interview-150
# References:
#   - https://www.geeksforgeeks.org/window-sliding-technique/
#   - https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/ introduces O(n^3), O(n^2), O(nlogn), and O(n) way for variable sized window.

from typing import List

# The concept is totally same as the algorithm introduced in https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return self.order_of_n_log_n(target, nums)
        return self.order_of_n(target, nums)

    def order_of_n(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        size = len(nums)
        _sum = 0

        result = size + 1

        while right < size:
            _sum += nums[right]
            if _sum >= target:
                while _sum - nums[left] >= target:
                    _sum -= nums[left]
                    left += 1

                result = min(result, right - left + 1)

            right += 1

        return result if result <= size else 0

    def order_of_n_log_n(self, target: int, nums: List[int]) -> int:
        pass

if __name__ == '__main__':
    s = Solution()
    result = s.minSubArrayLen(
        7,
        [2,3,1,2,4,3]
    )
    print(result)
