class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = 0
                for k in range(i, j):
                    if s[k] == s[k+1]:
                        c+=1
                if c <= 1:
                    res = max(j-i+1, res)
        return res