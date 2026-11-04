from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        # Two heaps to maintain the median
        left = []   # Max heap (negative values)
        right = []  # Min heap

        delayed = defaultdict(int)

        left_size = right_size = 0
        left_sum = right_sum = 0

        def prune(heap):
            while heap:
                val = -heap[0] if heap is left else heap[0]

                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal left_size, right_size
            nonlocal left_sum, right_sum

            while left_size > right_size + 1:
                val = -heapq.heappop(left)
                heapq.heappush(right, val)

                left_size -= 1
                right_size += 1
                left_sum -= val
                right_sum += val

            while left_size < right_size:
                val = heapq.heappop(right)
                heapq.heappush(left, -val)

                left_size += 1
                right_size -= 1
                left_sum += val
                right_sum -= val

            prune(left)
            prune(right)

        def add(val):
            nonlocal left_size, right_size
            nonlocal left_sum, right_sum

            if not left or val <= -left[0]:
                heapq.heappush(left, -val)
                left_size += 1
                left_sum += val
            else:
                heapq.heappush(right, val)
                right_size += 1
                right_sum += val

            rebalance()

        def remove(val):
            nonlocal left_size, right_size
            nonlocal left_sum, right_sum

            prune(left)
            prune(right)

            delayed[val] += 1

            if val <= -left[0]:
                left_size -= 1
                left_sum -= val

                if val == -left[0]:
                    prune(left)
            else:
                right_size -= 1
                right_sum -= val

                if right and val == right[0]:
                    prune(right)

            rebalance()

        def get_cost():
            median = -left[0]

            return (
                median * left_size - left_sum
                + right_sum - median * right_size
            )

        # Calculate the cost of every window of length x
        costs = []

        for i in range(x):
            add(nums[i])

        costs.append(get_cost())

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])

            costs.append(get_cost())

        # DP: prev[i] = minimum cost using j-1
        # subarrays among the first i elements
        INF = float("inf")
        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Skip the current element
                curr[i] = curr[i - 1]

                # Select a subarray ending at i-1
                if i >= x:
                    start = i - x

                    if prev[start] != INF:
                        curr[i] = min(
                            curr[i],
                            prev[start] + costs[start]
                        )

            prev = curr

        return prev[n]