from typing import List
from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        total = sum(diff)
        if k >= total:
            return 0

        cnt = Counter(diff)
        max_diff = max(cnt)

        while k > 0 and max_diff > 0:
            c = cnt[max_diff]
            use = min(k, c)

            cnt[max_diff] -= use
            cnt[max_diff - 1] += use

            if cnt[max_diff] == 0:
                max_diff -= 1

            k -= use

        ans = 0
        for d, c in cnt.items():
            ans += d * d * c
        return ans