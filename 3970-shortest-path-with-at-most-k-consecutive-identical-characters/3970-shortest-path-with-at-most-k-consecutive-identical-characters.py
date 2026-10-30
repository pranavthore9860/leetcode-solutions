from collections import defaultdict
import heapq
from typing import List


class Solution:

  def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))

    # Dijkstra on state: (weight, node, count)
    # Priority queue stores (weight, node, count)
    pq = [(0, 0, 1)]
    # Distance dictionary mapping (node, count) to min weight
    dist = {}

    while pq:
      w, u, count = heapq.heappop(pq)

      if u == n - 1:
        return w

      if (u, count) in dist and dist[(u, count)] < w:
        continue
      dist[(u, count)] = w

      for v, weight in adj[u]:
        next_char = labels[v]
        curr_char = labels[u]

        # If next node has the same label as current node, increment count
        # Otherwise, reset count to 1
        if next_char == curr_char:
          next_count = count + 1
        else:
          next_count = 1

        if next_count <= k:
          next_w = w + weight
          if (v, next_count) not in dist or next_w < dist[(v, next_count)]:
            dist[(v, next_count)] = next_w
            heapq.heappush(pq, (next_w, v, next_count))

    return -1