class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while r > l:
            m = (l +r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l + 1 if nums[l] < target else l