import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = list(args.input)

def letters_combination_of_phone_number(digits) -> int:

  phone_dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
  if digits == "":
    return []
  
  numbers = list(phone_dict[digits[0]])
  
  for digit in digits[1:]:
    numbers = [old + new for old in numbers for new in list(phone_dict[digit])]
      
  return numbers
              

print ( letters_combination_of_phone_number(list1))