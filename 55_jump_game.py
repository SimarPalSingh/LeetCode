from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
#       Below is a Greedy solution - going right to left!        
        
        lastIndexPosition = len(nums) - 1
        
        for i in range(len(nums)-1, -1 , -1):
            # We are trying to check if the last index position can be reached usign the i'th position!
            if ((i + nums[i]) >= lastIndexPosition): # i + nums[i] as the from position i you can jump nums[i] places at max !!
                lastIndexPosition = i # this is the last index position you can get to - that would eventually take you to the lst index position. This keeps on getting updated as long as we keep on fifing a position that can reach the last index position
        
        return lastIndexPosition == 0

print(Solution().canJump([2,2,0,1,4]))