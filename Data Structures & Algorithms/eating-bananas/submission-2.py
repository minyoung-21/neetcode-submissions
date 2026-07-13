class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 #left
        r = max(piles) #right
        piles.sort()

        while l <= r:
            time_taken = 0
            m = int((l+r)/2)
            for n in piles:
                time_taken += math.ceil(n / m)

            if time_taken <= h:
                r = m-1
            else:
                l = m+1
        
        return l