class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        zero = False
        while 0 in nums:
            zero = True
            nums.remove(0)
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            if nums[0] < 0 and zero:
                return 0
            return nums[0]
        res = 1
        m = -10
        for n in nums:
            res *= n
            if n < 0:
                m = max(m, n)
        return res if res > 0 else res // m