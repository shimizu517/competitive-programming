# From https://leetcode.com/problems/remove-element
# Submission: https://leetcode.com/problems/remove-element/submissions/1336114976/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        k = 0
        for num in nums:
            if num != val:
                k += 1
                nums[r] = num
                r += 1

        return k
