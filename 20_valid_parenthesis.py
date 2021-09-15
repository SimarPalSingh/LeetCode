import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = args.input
list1 = "()"
def valid_parenthesis(self, s: str) -> bool:
  stack = []
  dict = {"]":"[", "}":"{", ")":"("}
  
  for char in s:
    if char in dict.values():
        stack.append(char)
    elif char in dict.keys():
      if stack == [] or dict[char] != stack.pop():
        return False
    else:
      return False

  return stack == []

print (valid_parenthesis(0, list1))
