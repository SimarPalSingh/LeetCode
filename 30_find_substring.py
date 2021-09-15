class Solution:
  def permute(self, nums) -> list[list]:
    result = []
    if len(nums) == 1:
      return [nums[:]]
    
    for i in range(len(nums)):
      n = nums.pop(0)
      # recursive - backtracking
      perms = self.permute( nums)
      
      for perm in perms:
        perm.append(n)
      result.extend(perms)
      nums.append(n)   
        
    return result
  
  def findSubstring(self, s: str, words: list) -> list:
    out = []
    set1 = self.permute(words)
    print(set1)
    for sbs in set1:
      if ''.join(sbs) in s:
        out.append(s.find(''.join(sbs)))
    
    return out

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))