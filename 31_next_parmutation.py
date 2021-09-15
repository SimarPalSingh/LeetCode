class Solution:
    #  function to swap two numbers/elements in the list
    def swap(self, nums: list[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i]=nums[j]
        nums[j]=temp
    #  function to reverse the lsit from start till end - Last step in the algorithm
    def reverse(self, nums: list[int], start: int) -> None:    
        i = start 
        j = len(nums) - 1
        while i<j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
    # main function       
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2 # intialised to second last element
        # locating the index in the list where nums[i] >= nums[i+1]
        while (i >= 0 and nums[i+1] <= nums[i]):    
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1 # intialised to last element
            while nums[j] <= nums[i]: #finding the element just greater than nums[i]
                j -= 1
            
            self.swap( nums, i , j) # swapping nums[i] and nums[j]
        
        self.reverse( nums, i+1) # reversing all the numbers till nums[i]
        
nums = "3,2,1".split(",") # Sample Input
Solution().nextPermutation(nums)
print(nums)