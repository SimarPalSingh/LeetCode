from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  BEST Solution beats 90%
        return Counter(s) ==  Counter(t)
        
        #  not any better than the solution below
        # if len(s) != len(t):
        #     return False
        
        # for x in s:
        #     if x in t:
        #         t = t.replace(x,"",1)
        #     else:
        #         return False
        # # print (t.strip())
        # if len(t.strip()) != 0:
        #     return False
        
        return True
        # the below implementation was better than 9 %
        # if len(s) != len(t):
        #     return False
        # dict = {}
        # for x in s:
        #     if x in dict.keys():
        #         # dict[x] += 1
        #         dict.update({x: dict.get(x) + 1})
        #     else:
        #         dict.update({x: 1})
        #         # dict.add(x, 1)
        
        # for x in t:
        #     if x in dict.keys():
        #         if (dict.get(x) > 1):
        #             dict.update({x: dict.get(x) - 1})
        #         elif (dict.get(x) == 1):
        #             dict.pop(x)
        #     else:
        #         return False
        # print(dict)
        # if len(dict.keys()) == 0:
        #     return True
        # else:
        #     return False


print(Solution().isAnagram("aacc", "ccac"))