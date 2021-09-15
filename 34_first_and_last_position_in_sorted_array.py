import math
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums)-1
        if len(nums) == 1 and nums[0]==target:
            return [0,0]
        # if nums[l] > target or nums[r] < target:
        #     return [-1,-1]
        
        while l <= r:
            m = math.ceil((l+r)/2)
            if nums[m] == target:
                l = m
                r = m
                while  l>0 and nums[l-1] == target:
                    l -= 1
                while (r<len(nums)-1) and nums[r+1] == target:
                    r += 1      
                return [l,r]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1,-1]
# nums = "3,2,1".split(",") # Sample Input
nums = [5,7,7,8,8,10]
target = 8
print (Solution().searchRange(nums, target))
