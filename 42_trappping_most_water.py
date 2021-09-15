import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    
height=[]
height = (args.input.split(","))

# Sample --input "1,8,6,2,5,4,8,3,7"
def trapping_most_water(height):
  l=0
  r=len(height) - 1
  maxL=int(height[l])
  maxR=int(height[r])
  res=0
  while l<r:
    if(maxL<maxR):
      l += 1
      maxL = max(maxL,int(height[l]))
      res += maxL - int(height[l])
    else:
      r -= 1
      maxR = max(maxR,int(height[r]))
      res += maxR - int(height[r])
  
  print(res)
          
trapping_most_water(height)