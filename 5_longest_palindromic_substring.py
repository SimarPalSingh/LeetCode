import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

s = args.input


def longest_palindromic_substring(s: str):
  res=""
  resLen=0
  l=r=0
  for i in range(len(s)):
      #odd test cases
    l=r=i
    while (l >= 0 and r<len(s) and s[l]==s[r]):
      if((r-l+1) > resLen):
        res = s[l:r+1]
        resLen = r - l + 1
      l -= 1
      r += 1
      
      #even test cases
    l=i
    r=i+1
    while (l >= 0 and r<len(s) and s[l]==s[r]):
      if((r-l+1) > resLen):
        res = s[l:r+1]
        resLen = r - l + 1
      l -= 1
      r += 1
          
  print(res)

longest_palindromic_substring(s)