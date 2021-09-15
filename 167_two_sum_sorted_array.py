import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

list = (args.input.split(","))
target = int(args.target)

# Sample --input "["flower","flow","flight"]" Solution = "fl"
def two_sum_sorted_array(numbers, target) -> str: 
    
  
  
  # INITIAL SOLUTION - BASED ON THE TWO SUM PROBLEM
  # dict ={}        
  # for i in range(1, len(numbers)+1):
  #   if numbers[i-1] in dict:
  #     return dict.get(numbers[i-1]),i
  #   else:
  #     output = target - int(numbers[i-1])
  #     dict[output] = i
        
  # return []

print ("Solution: " + two_sum_sorted_array(list, target))