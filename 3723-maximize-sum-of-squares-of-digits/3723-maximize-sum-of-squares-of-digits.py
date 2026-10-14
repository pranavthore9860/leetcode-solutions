class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum < 1:
            return ""

        q, r = divmod(sum, 9)

        if q == num:
            return "9" * num

        ans = ["9"] * q
        if r:
            ans.append(str(r))
        ans.extend("0" * (num - len(ans)))

        return "".join(ans)