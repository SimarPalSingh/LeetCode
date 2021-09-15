from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # initialising a default dic t with values as list

        for s in strs:
            count = [0] * 26 # a ... z # count is an array for 25 elements

            for c in s:
                count[ord(c) - ord("a")] += 1 # storing a as count[0] and z as count[25]

            res[tuple(count)].append(s) # since lists are immutable, has to be cinverted to tuple
        
        return res.values()


print (Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))