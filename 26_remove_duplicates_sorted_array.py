import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


# list1 = args.input.split(",")
list1 = "0,0,1,1,1,2,2,3,3,4"
def removeDuplicates(nums) -> int:
  if len(nums) == 0:
    return 0
        
  i = 0
  
  for j in range(1, len(nums)):
    if nums[j] != nums[i]:
      i += 1
      nums[i] = nums[j]
          
  return i + 1

print (removeDuplicates(list1))