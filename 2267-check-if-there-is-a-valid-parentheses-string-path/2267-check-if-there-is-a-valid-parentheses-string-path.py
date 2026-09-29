from functools import lru_cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # First must be '(' and last must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # Path length must be even for a valid parentheses string
        if (m + n - 1) % 2 == 1:
            return False

        @lru_cache(None)
        def dfs(i: int, j: int, bal: int) -> bool:
            if grid[i][j] == '(':
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                return False

            rem = (m - 1 - i) + (n - 1 - j)
            if bal > rem + 1:
                return False

            if i == m - 1 and j == n - 1:
                return bal == 0

            if i + 1 < m and dfs(i + 1, j, bal):
                return True
            if j + 1 < n and dfs(i, j + 1, bal):
                return True

            return False

        return dfs(0, 0, 0)