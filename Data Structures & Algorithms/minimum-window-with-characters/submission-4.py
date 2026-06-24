class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm1 = {}
        hm2 = {}
        res = ""
        l, r = 0, 0

        if len(t) > len(s):
            return res

        while r < len(t):
            if t[r] in hm1.keys():
                hm1[t[r]] += 1
            else:
                hm1[t[r]] = 1
            
            r += 1

        r = 0
        need, have = len(hm1), 0
        min_len = 1001

        while r < len(s):
            
            if s[r] in hm1.keys():
                if s[r] in hm2.keys():
                    hm2[s[r]] += 1
                else:
                    hm2[s[r]] = 1
                
                if hm2[s[r]] == hm1[s[r]]:
                    have += 1
            
            # shrink
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]

                if s[l] in hm1:
                    hm2[s[l]] -= 1
                    if hm2[s[l]] < hm1[s[l]]:
                        have -= 1

                l += 1

            r += 1
        return res