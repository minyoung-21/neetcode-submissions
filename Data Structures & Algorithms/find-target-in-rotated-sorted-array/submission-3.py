class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            # middle value is in the left portion (bigger)
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    # target is in the left
                    r = m - 1
                else:
                    # target is in the right
                    l = m + 1
            elif nums[l] > nums[m]:
                # middle value is in the right portion (smaller)
                if nums[m] < target <= nums[r]:
                    # target is in the right
                    l = m + 1
                else:
                    # target is in the left
                    r = m - 1
            
        return -1