from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        vals = sorted(x * x for x in nums)

        m = (len(nums) + 1) // 2
        return sum(vals[-m:]) - sum(vals[:-m])