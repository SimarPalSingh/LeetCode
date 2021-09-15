import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

list = (args.input.split(","))

# Sample --input "["flower","flow","flight"]" Solution = "fl"
def longest_common_prefix(self, strs) -> str:
        
  if (len(strs) == 0):
      return ""
  if (len(strs) == 1):
      return strs[0]
        
  lcs = strs[0]
  len_lcs = len(strs[0])
  
  for s in strs[1:]:
    while lcs != s[0:len_lcs]:
      lcs = lcs[0:len_lcs - 1]
      len_lcs -= 1
      
      if(len_lcs == 0):
        return ""
  
  return lcs
                
  # my initial solution 
#        lcs = min(strs, key=len)
#         len_of_lcs = len(lcs)
#         for i in range(0, len_of_lcs ):
# #             (all(lcs in flag  for (flag) in strs)):
#             if (all(flag.startswith(lcs) == True for (flag) in strs)):
#                 return lcs
#             else:
#                 # lcs = lcs.rstrip(lcs[-1])
#                 lcs = lcs[:len_of_lcs - (i+1)]

#         return ""


print ("Solution: " + longest_common_prefix('', list))