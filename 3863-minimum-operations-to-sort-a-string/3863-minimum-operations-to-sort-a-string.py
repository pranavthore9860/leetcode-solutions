class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        for i in range(1, len(s) - 1):
            if s[i] == min_char or s[i] == max_char:
                return 2
                
        return 3