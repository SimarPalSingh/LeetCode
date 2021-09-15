import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    

x = args.input
def my_atoi(s: str):
  s = s.lstrip()
  if (len(s)<1):
    print (0)
  negative = False
  if (s[0] == "-"):
    negative = True
    s = s[1:len(s)]
  elif (s[0] == "+"):
    negative = False
    s = s[1:len(s)]
  
  value = 0
  for i in range(len(s)):
    if(s[i].isnumeric()):
      value = value*10 + int(s[i])
    else:
      if(value > 0):
        if(negative):
          if (value > pow(2,31)):
            print (-pow(2,31))
            exit()
          else:
            print (-value)
            exit()
        else:
          if (value > pow(2,31) - 1):
            print (pow(2,31) - 1)
            exit()
          else:
            print (value)
            exit()
      else:
        print (0)
        exit()
          
  if(negative):
    if (value > pow(2,31)):
      print (-pow(2,31))
    else:
      print (-value)
  else:
    if (value > pow(2,31) - 1):
      print (pow(2,31) - 1)
    else:
      print (value)
          
my_atoi(x)