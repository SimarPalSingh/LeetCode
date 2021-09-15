import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

x = int(args.input)
def reversed_integer(x: int):
  current = x
  reversed = 0
  temp = 0
  negative = False
# negative test cases
  if (x < 0):
    negative = True
    current = -x
  while (current >= 1):
    temp = current%10
    reversed = reversed * 10 + temp
    current = math.floor(current/10)
  
  if (reversed > pow(2,31)):
    print (0)
  if(negative):
    print (-reversed)
  else:
    print (reversed)
          
reversed_integer(x)