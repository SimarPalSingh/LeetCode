import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


# list1 = args.input.split(",")
nums = "3,2,2,3".split(",")
val = 3
def removeElement(nums, val: int) -> int:
  i = 0
  n = len(nums)
  while i < n:
    if int(nums[i]) == val:
      nums[i] = nums[n - 1]
      n -= 1;
    else:
      i += 1
  return n
        

print (removeElement(nums, val))