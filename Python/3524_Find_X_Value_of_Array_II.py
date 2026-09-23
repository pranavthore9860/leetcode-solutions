from typing import List

class Node:
    __slots__ = ("remain", "prod")

    def __init__(self, k):
        self.remain = [0] * k
        self.prod = 1


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, nums)

    def merge(self, L, R):
        node = Node(self.k)
        node.prod = (L.prod * R.prod) % self.k

        for i in range(self.k):
            node.remain[i] = L.remain[i]

        for i in range(self.k):
            node.remain[(i * L.prod) % self.k] += R.remain[i]

        return node

    def build(self, idx, l, r, nums):
        if l == r:
            self.tree[idx].prod = nums[l]
            self.tree[idx].remain[nums[l]] = 1
            return

        m = (l + r) // 2
        self.build(idx * 2 + 1, l, m, nums)
        self.build(idx * 2 + 2, m + 1, r, nums)
        self.tree[idx] = self.merge(
            self.tree[idx * 2 + 1],
            self.tree[idx * 2 + 2],
        )

    def update(self, idx, l, r, pos, val):
        if l == r:
            self.tree[idx] = Node(self.k)
            self.tree[idx].prod = val
            self.tree[idx].remain[val] = 1
            return

        m = (l + r) // 2
        if pos <= m:
            self.update(idx * 2 + 1, l, m, pos, val)
        else:
            self.update(idx * 2 + 2, m + 1, r, pos, val)

        self.tree[idx] = self.merge(
            self.tree[idx * 2 + 1],
            self.tree[idx * 2 + 2],
        )

    def query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[idx]

        if qr < l or r < ql:
            return Node(self.k)

        m = (l + r) // 2

        if qr <= m:
            return self.query(idx * 2 + 1, l, m, ql, qr)
        if ql > m:
            return self.query(idx * 2 + 2, m + 1, r, ql, qr)

        left = self.query(idx * 2 + 1, l, m, ql, qr)
        right = self.query(idx * 2 + 2, m + 1, r, ql, qr)
        return self.merge(left, right)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        nums = [x % k for x in nums]
        for q in queries:
            q[1] %= k

        st = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            st.update(0, 0, st.n - 1, idx, val)
            node = st.query(0, 0, st.n - 1, start, st.n - 1)
            ans.append(node.remain[x])

        return ans