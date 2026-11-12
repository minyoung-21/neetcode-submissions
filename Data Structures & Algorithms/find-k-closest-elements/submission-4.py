import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        r = bisect.bisect_right(arr, x)
        l = r-1
        n = len(arr)
        res = []

        for _ in range(k):
            # no left candidate
            # move to right
            if l < 0:
                r += 1
            # no right candidate
            # move to left
            elif r >= n:
                l -= 1
            elif arr[r] - x >= x - arr[l]:
                # left is closer
                l -= 1
            else:
                r += 1
        
        return arr[l+1 : r]