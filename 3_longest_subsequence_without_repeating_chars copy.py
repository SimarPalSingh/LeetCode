import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = args.input

def lengthOfLongestSubstring(s: str) -> int:
  lols = 0
  sub = ""
  l = 0
  index = 0
  for char in s:
    # print(char)
    # print(sub)
    if char not in sub:
      sub += char
      l = len(sub)
      if l > lols:
        lols = l
    else:
      index = sub.find(char)
      l = len(sub)
      if l > lols:
        lols = l
      sub += char
      sub = sub [index+1:]
  return lols

print (lengthOfLongestSubstring("aabaab!bb"))

# [2,4,3]  "aabaab!bb"
# [5,6,4]