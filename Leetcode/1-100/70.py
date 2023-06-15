class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, res = 1, 1, 1
        for i in range(1, n):
            res = a + b
            a, b = b, res
        return res