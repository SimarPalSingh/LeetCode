import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

num = int(args.input)

# Sample --input "1,8,6,2,5,4,8,3,7"
def integer_to_roman(num):
  res=""
  divisors = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V" , 4: "IV"}
  for d in divisors:
    if num/d >= 1:
      for x in range(0, int(num/d)):
        res += divisors[d]
      num %= d

  
  for i in range(0,num):
    res += "I"

  print(res)
          
integer_to_roman(num)