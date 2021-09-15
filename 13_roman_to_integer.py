import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

num = (args.input)

# Sample --input "1,8,6,2,5,4,8,3,7"
def roman_to_integer(s):
  res=0
  divisors = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40,"X":10, "IX":9, "V":5, "IV":4, "I":1}
  
  for d in divisors:
    if s.startswith(d):
      for i in range(0,s.count(d)):
        if s.startswith(d):
          s = s.replace(d,"",1)
          res += divisors[d]
  # return res

  print(res)
          
roman_to_integer(num)