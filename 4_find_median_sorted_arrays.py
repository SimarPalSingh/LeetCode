import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = args.input

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    median = 0.0
    final = nums1 + nums2
    final.sort()
    length = len(final)
    if length % 2 == 0:
      a = int(length/2 - 1)
      b = int(length/2)
      median = (final[a] + final[b]) / 2
    else:
      b = int(length/2)
      median = (final[b])
    return median

print (findMedianSortedArrays([1]]))

# [2,4,3]  "aabaab!bb"
# [5,6,4]