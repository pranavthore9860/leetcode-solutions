from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0
            x = num

            while x > 0:
                digit_sum += x % 10
                x //= 10

            if digit_sum == i:
                return i

        return -1