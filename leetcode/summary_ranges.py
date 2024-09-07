# From: https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return self.nested_while_solution(nums)

    def nested_while_solution(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = []
        i = 0
        while i < len(nums):
            left = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1

            result.append(self.__generate_result_str(
                left=left,
                right=nums[i],
            ))
            i += 1

        return result


    def my_solution(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f'{nums[0]}']

        cur = nums[0]
        li = 0  # pointer to the most left item in a array that meets the condition.
        result = []

        for i in range(1, len(nums)):
            if cur + 1 == nums[i]:
                cur = nums[i]
                continue

            # Process when the subarray doesn't meet the condition.
            result.append(self.__generate_result_str(
                left=nums[li],
                right=cur,
            ))
            li = i
            cur = nums[i]

        # Need to append item because the last cur and li is not stored in the for loop.
        result.append(self.__generate_result_str(
            left=nums[li],
            right=cur,
        ))
        return result

    def __generate_result_str(self, left: int, right: int) -> str:
        if left == right:
            return f'{left}'
        return f'{left}->{right}'
