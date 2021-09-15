import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    
height=[]
height = (args.input.split(","))

# Sample --input "1,8,6,2,5,4,8,3,7"
def container_with_most_water(height):
  l=0
  r=len(height)-1
  maxArea=0
  while (l<r):
    maxArea = max(maxArea, (r-l)*(min(int(height[l]),int(height[r]))))
    if(int(height[l])<int(height[r])):
      l += 1
    else:
      r -=1
  
  print (maxArea)
          
container_with_most_water(height)