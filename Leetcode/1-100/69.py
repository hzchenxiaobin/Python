class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, 0
        while r >= l:
            m = (l + r) // 2
            v = m ** 2
            if v <= x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans