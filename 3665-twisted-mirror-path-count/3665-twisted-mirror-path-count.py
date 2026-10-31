from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(i, j, dx, dy):
            x, y = i + dx, j + dy

            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 0:
                    return x, y

                # Reflect at the mirror
                if dx == 0:       # Moving right
                    dx, dy = 1, 0  # Turn down
                else:             # Moving down
                    dx, dy = 0, 1  # Turn right

                x += dx
                y += dy

            return -1, -1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                # Move right
                x, y = move(i, j, 0, 1)
                if x != -1:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

                # Move down
                x, y = move(i, j, 1, 0)
                if x != -1:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]