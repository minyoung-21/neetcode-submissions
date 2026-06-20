class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            med = l + (r - l) // 2
            
            if nums[med] > target:
                r = med 
            elif nums[med] < target:
                l = med +1 
            
            else:
                return med
        
        return -1