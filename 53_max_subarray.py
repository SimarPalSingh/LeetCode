class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        maxSum = -100000
        for i in range(len(nums)):
            current = max(nums[i], current + nums[i])
            
            maxSum = max(maxSum, current)
        return maxSum

print (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # returns 6 as the maximun subarray!