import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = list(args.input)

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

  def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
    res = []
    if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
      return res
    if k == 2:
      return twoSum(nums, target)

    for i in range(len(nums)):
      if i == 0 or nums[i - 1] != nums[i]:
        for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
          res.append([nums[i]] + subset)

    return res

  def twoSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    lo, hi = 0, len(nums) - 1

    while (lo < hi):
      curr_sum = nums[lo] + nums[hi]
      if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
        lo += 1
      elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
        hi -= 1
      else:
        res.append([nums[lo], nums[hi]])
        lo += 1
        hi -= 1
                                                  
    return res

nums.sort()
print(kSum(nums, target, 4))
              

print ( four_sum(list1))