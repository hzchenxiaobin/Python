# class Solution:
#     def makeSmallestPalindrome(self, s: str) -> str:
#         n = len(s)
#         s = list(s)
#         for i in range(0, n // 2):
#             if s[i] == s[n - 1 - i]:
#                 continue
#             if s[i] < s[n-1-i]:
#                 s[n-1-i] = s[i]
#             else:
#                 s[i] = s[n-1-i]
#         return ''.join(s)

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        s = list(s)
        for i in range(0, n // 2):
            s[n-1-i] = min(s[i], s[n-1-i])
            s[i] = min(s[i], s[n-1-i])
        return ''.join(s)  