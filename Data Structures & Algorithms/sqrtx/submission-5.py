class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0

        if x == 0:
            return res

        while l <= r:
            m = l + (r - l) // 2
            if m * m < x:
                res = m
                l = m + 1
            elif x/m == m:
                return m
            else:
                r = m - 1
            
        return math.floor(res)