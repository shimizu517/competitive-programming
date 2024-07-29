# From: https://leetcode.com/problems/majority-element/description
# Submission: https://leetcode.com/problems/majority-element/submissions/1336908740

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        criteria = len(nums) // 2
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] > criteria:
                return num
