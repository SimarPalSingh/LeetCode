class Solution:
  def divide( dividend: int, divisor: int) -> int:
    flag = False
    output = 0
    d = abs(dividend)
    dv = abs(divisor)
    
#   main loop
    while d >= dv:
      tmp = dv
      mul = 1
      while d >= tmp:
        d -= tmp
        output += mul
        mul +=mul
        tmp += tmp
    
#   if one of them is negative
    if (( divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0)):
      output = -output
    
    return max(-2147483648,min(output,2147483647)) # boundary coniditions

print (Solution.divide(20, 3))