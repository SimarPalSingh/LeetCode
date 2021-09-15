import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = args.input

def zig_zag_conversion(s, numRows) -> float:
  up = True
  dicts = {}
  circularLen = 0

  for i in range(0, len(s)):
    if up:
      circularLen += 1
    else:
      circularLen -= 1
    if(circularLen in dicts.keys()):   
      dicts[circularLen] += s[i]
    else:
      dicts[circularLen] = s[i]
    
    if(circularLen == numRows):
      up = False
    if (circularLen == 1 ):
      up = True
  output = ""

  for x in dicts.keys():
    print(x)
    print(dicts[x])
    output += dicts[x]
  
  return output

print (zig_zag_conversion("PAYPALISHIRING",3))

# [2,4,3]  "aabaab!bb"
# [5,6,4]