class Solution:
    def findMin(self, nums: List[int]) -> int:
        # maybe the min is almost always next to the max
        # we can wrap if the max is at the end of the arr

        l = 0
        r = len(nums) - 1

        min_num = 1001

        while l <= r:
            m = l + (r - l) // 2
            min_num = min(min_num, nums[m])
            if nums[l] < nums[r]:
                # it's in the order we want
                min_num = min(min_num, nums[l])
                break
            if nums[r] > nums[m]:
                # the other sorted part of the arr is between r and m
                r = m - 1
            else:
                l = m + 1
             
        return min_num