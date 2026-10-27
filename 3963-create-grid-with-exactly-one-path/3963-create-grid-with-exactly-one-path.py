class Solution:

  def createGrid(self, m: int, n: int) -> list[str]:
    grid = []

    for i in range(m):
      if i < m - 1:
        # Only the first cell is free; the rest of the row is blocked
        grid.append("." + "#" * (n - 1))
      else:
        # The last row is entirely free
        grid.append("." * n)

    return grid