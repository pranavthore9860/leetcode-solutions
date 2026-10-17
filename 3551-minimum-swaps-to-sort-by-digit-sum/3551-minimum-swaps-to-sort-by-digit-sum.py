from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {value: i for i, value in enumerate(nums)}
        target = [position[x] for x in sorted_nums]

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or target[i] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[j]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps