import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


# list = (args.input.split(" "))
# target = int(args.target)
list=[-1,2,1,-4]
target = 1

def three_sum_closest(nums, target) -> int:

  best_sum = 10000000
  nums.sort() # inplacce SORT
  
  for i in range(0,len(nums) - 2):
      
    if  i > 0 and nums[i] ==  nums[i-1]:
      continue

    l = i+1
    r = len(nums) - 1
    
    while l < r:
        
      currSum = nums[i] + nums[l] + nums[r]
      
      if(currSum == target):
        return target
      
      if abs(target - currSum) < abs(target - best_sum):
        best_sum = currSum
      
      if(currSum <= target):
        l += 1
        while nums[l] ==  nums[l-1] and l < r:
          l += 1
      else:
        r -= 1
          
  return best_sum  
              

print ( three_sum_closest(list, target))