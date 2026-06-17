class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        hm1 = {}
        hm2 = {}

        str_len = len(s1)

        if len(s1) > len(s2):
            return False

        while r < str_len:
            if s1[r] not in hm1.keys():
                hm1[s1[r]] = 1
            else:
                hm1[s1[r]] += 1

            r += 1
        
        k = len(s1)
        str_len = len(s2)
        r = 0

        while r < str_len:
            print(hm2)
            if r-l+1 > k:
                if hm2[s2[l]] == 1:
                    hm2.pop(s2[l])
                else:
                    hm2[s2[l]] -= 1
                l += 1

            if s2[r] not in hm2.keys():
                hm2[s2[r]] = 1
            else:
                hm2[s2[r]] += 1
            
            if hm1 == hm2:
                return True
            r += 1
        
        
        return False