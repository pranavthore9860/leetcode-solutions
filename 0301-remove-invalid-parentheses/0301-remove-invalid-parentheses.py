from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            cur = queue.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue
                nxt = cur[:i] + cur[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res