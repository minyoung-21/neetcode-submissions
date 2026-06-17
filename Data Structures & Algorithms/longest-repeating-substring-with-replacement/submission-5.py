class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        string_length = len(s)
        hm = {}

        while r < string_length:
            if s[r] not in hm.keys():
                hm[s[r]] = 1
            else:
                hm[s[r]] += 1
            
            if (r-l+1) - max(hm.values()) <= k:
                res = r - l + 1
                
            else:
                hm[s[l]] -= 1
                l += 1
            
            print(hm, s[l], l, s[r], r)
            r += 1
            
        return res