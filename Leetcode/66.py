class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []
        p = 1
        for i in range(n):
            v = p + digits[n - 1 - i]
            if v == 10:
                p = 1
                v = 0
            else:
                p = 0
            res.append(v)
        if p == 1:
            res.append(1)
        res.reverse()
        return res
