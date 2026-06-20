class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            med = l + (r - l) // 2 
            print(med)
            if nums[med] > target:
                r = med - 1
            elif nums[med] < target:
                l = med + 1
            else:
                return med
        
        return -1