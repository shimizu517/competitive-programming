import math


class Solution:
    def findSubarray(self, a, n):
        low, high, sum = self.find_maximum_subarray(a, 0, n - 1)
        return a[low : high + 1]

    def find_maximum_subarray(self, a, low, high):
        if high == low:
            return (low, high, a[low])
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = self.find_maximum_subarray(a, low, mid)
        right_low, right_high, right_sum = self.find_maximum_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(
            a, low, mid, high
        )
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    def find_max_crossing_subarray(self, a, low, mid, high):
        left_sum = -(10 ** 6)
        sum = 0
        max_left = -(10 ** 6)
        for i in range(mid, low - 1, -1):
            sum += a[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        right_sum = -(10 ** 6)
        sum = 0
        max_right = -(10 ** 6)
        for i in range(mid + 1, high + 1):
            sum += a[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i
        return (max_left, max_right, left_sum + right_sum)


s = Solution()
a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(s.findSubarray(a, len(a)))
