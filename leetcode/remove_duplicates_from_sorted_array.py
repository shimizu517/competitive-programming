# From: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description
# Submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1336901610

from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        right = 0
        count_dict = defaultdict(int)
        for num in nums:
            if count_dict[num] <= 1:
                count_dict[num] += 1
                nums[right] = num
                right += 1
                k += 1
        return k
