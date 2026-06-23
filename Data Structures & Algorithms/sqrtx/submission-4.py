class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        arr = []
        if x == 0:
            return res

        while l <= r:
            m = l + (r - l) // 2
            arr.append(x / m)
            if m * m < x:
                res = m
                l = m + 1
            elif x/m == m:
                return m
            else:
                r = m - 1
            
        print(arr)
        return math.floor(res)