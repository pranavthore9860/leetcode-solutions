class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = []

        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = []
            elif ch == ')':
                curr.reverse()
                prev = stack.pop()
                curr = prev + curr
            else:
                curr.append(ch)

        return "".join(curr)