
# class Solution:
#     def minLength(self, s: str) -> int:
#         while s.find("AB") != -1 or s.find("CD") != -1:
#             s = s.replace("AB", "")
#             s = s.replace("CD", "")
#         return len(s)

class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "").replace("CD", "")
        return len(s)