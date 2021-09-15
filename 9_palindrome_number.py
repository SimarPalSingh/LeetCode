import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

x = int(args.input)

# This code works with PYthon on LeetCode but not with Python3!!
def palindrome_number(x: int):
  if(x <  0 or (x % 10 == 0 and x!=0)):
    print("false")
        
  rev = 0

  while (x > rev):
    rev = math.floor(rev*10 + x%10)
    print( rev)
    x = math.floor(x/10)       
    print( x)
  
  if (x == rev):
    print("True")
  if (x==rev/10):
    print("True")
          
palindrome_number(x)