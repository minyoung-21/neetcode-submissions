class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = l + (r - l) // 2
            hour_count = 0
            for p in piles:
                # if p % m == 0:
                #     # no remainder
                #     hour_count += p // m
                # else:
                #     # has remainder
                #     hour_count += p // m + 1
                hour_count += math.ceil(p / m)
            if hour_count > h:
                l = m + 1
            elif hour_count <= h:
                r = m - 1
                res = min(m, res)
            
        return res