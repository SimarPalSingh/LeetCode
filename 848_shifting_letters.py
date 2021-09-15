from collections import defaultdict
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        N = len(s)
        running_sum = 0
        ans = [None] * N
        offset = ord('a')

        for i in range(N-1, -1, -1):
            running_sum += shifts[i]
            ans[i] = chr((((ord(s[i]) - offset) + running_sum) % 26) + offset)
            
        return ''.join(ans)

print (Solution().shiftingLetters("abc",[10,20,30]))