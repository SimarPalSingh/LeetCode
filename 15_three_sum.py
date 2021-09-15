import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

list = (args.input.split(","))

# Sample --input "["flower","flow","flight"]" Solution = "fl"
def three_sum(nums) -> list:
        
  solution =[]
  nums.sort()
  l=0
  r = len(nums) - 1
  for i in range(0,len(nums)):
      
    if  i > 0 and nums[i] ==  nums[i-1]:
      continue
    l = i+1
    r = len(nums) - 1
    while l < r:
      currSum = nums[i] + nums[l] + nums[r]
      if(currSum < 0):
        l += 1  
      elif(currSum > 0):
        r -= 1
      else:
        solution.append([nums[i],nums[l],nums[r]])
        l += 1
        while nums[l] == nums[l-1] and l < r:
          l += 1
          
  return solution 
                
  # my initial solution 
#        lcs = min(strs, key=len)
#         len_of_lcs = len(lcs)
#         for i in range(0, len_of_lcs ):
# #             (all(lcs in flag  for (flag) in strs)):
#             if (all(flag.startswith(lcs) == True for (flag) in strs)):
#                 return lcs
#             else:
#                 # lcs = lcs.rstrip(lcs[-1])
#                 lcs = lcs[:len_of_lcs - (i+1)]

#         return ""


print ("Solution: " + three_sum(list))