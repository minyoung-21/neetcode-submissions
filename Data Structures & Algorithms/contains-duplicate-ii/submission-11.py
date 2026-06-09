class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = 1
        hs = set()
        hs.add(nums[l])

        if k == 0:
            return False

        while r < len(nums):
            
            if abs(r - l) > k:
                hs.remove(nums[l])
                l += 1
            
            if nums[r] in hs:
                return True;
            
            hs.add(nums[r])
            r += 1
        return False;