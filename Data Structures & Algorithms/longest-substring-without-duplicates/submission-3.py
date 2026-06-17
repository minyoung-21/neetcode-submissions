class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hs = set()
        res = 0

        if len(s) == 1:
            return 1

        while r < len(s):
            print(s[l], l, s[r], r)
            print(hs)
            if s[r] not in hs:
                hs.add(s[r])
                r += 1
            else:
                res = max(res, len(hs))
                hs.remove(s[l])
                
                l += 1
        
        res = max(res, len(hs))
        return res