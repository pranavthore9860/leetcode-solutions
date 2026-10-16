from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right, val):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                lazy[node] += val
                tree[node] += val * val * (end - start + 1)
                if start != end:
                    mid = (start + end) // 2
                    tree[node] += 2 * val * (
                        query_sum(node * 2, start, mid)
                        + query_sum(node * 2 + 1, mid + 1, end)
                    )
                tree[node] %= MOD
                lazy[node] %= MOD
                return

            push(node, start, end)
            mid = (start + end) // 2
            update(node * 2, start, mid, left, right, val)
            update(node * 2 + 1, mid + 1, end, left, right, val)
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        def query_sum(node, start, end):
            return (tree[node] + MOD) % MOD

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            val = lazy[node]
            mid = (start + end) // 2

            for child, length in (
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid),
            ):
                tree[child] = (
                    tree[child]
                    + 2 * val * query_sum(child, 0, 0)
                    + val * val * length
                ) % MOD
                lazy[child] = (lazy[child] + val) % MOD

            lazy[node] = 0

        # Use a segment tree storing both sums and squared sums.
        # A range increment x -> x+1 changes x² to x²+2x+1.
        sums = [0] * (4 * n)
        squares = [0] * (4 * n)
        pending = [0] * (4 * n)

        def apply(node, start, end, val):
            length = end - start + 1
            squares[node] = (
                squares[node] + 2 * val * sums[node] + val * val * length
            ) % MOD
            sums[node] = (sums[node] + val * length) % MOD
            pending[node] += val

        def push_down(node, start, end):
            if pending[node] == 0 or start == end:
                return
            mid = (start + end) // 2
            apply(node * 2, start, mid, pending[node])
            apply(node * 2 + 1, mid + 1, end, pending[node])
            pending[node] = 0

        def range_add(node, start, end, left, right):
            if left > end or right < start:
                return
            if left <= start and end <= right:
                apply(node, start, end, 1)
                return

            push_down(node, start, end)
            mid = (start + end) // 2
            range_add(node * 2, start, mid, left, right)
            range_add(node * 2 + 1, mid + 1, end, left, right)

            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        ans = 0
        last_seen = {}

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            range_add(1, 0, n - 1, prev + 1, i)
            ans = (ans + squares[1]) % MOD
            last_seen[x] = i

        return ans