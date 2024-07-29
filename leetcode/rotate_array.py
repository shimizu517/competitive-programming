# From: https://leetcode.com/problems/rotate-array
# Submission: https://leetcode.com/problems/rotate-array/submissions/1337043768

# Topic: array rotation, rotate array

# References:
# - https://www.geeksforgeeks.org/complete-guide-on-array-rotations/
# - https://www.geeksforgeeks.org/program-to-reverse-an-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        self.reversal_algorithm(nums, k)
    
    def reversal_algorithm(self, nums, k):
        # Without this line, error occurs when nums = [-1] and k = 2.
        k = k % len(nums)
        nums.reverse()
        self.reverse_subset(nums, 0, k - 1)
        self.reverse_subset(nums, k, len(nums) - 1)

    def reverse_subset(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
