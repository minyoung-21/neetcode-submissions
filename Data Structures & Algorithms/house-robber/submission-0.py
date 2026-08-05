class Solution:
    def rob(self, nums: List[int]) -> int:
        # we could either start from index 0 or 1
        n = len(nums)
        cache = [0] * (n+1)
        cache[1] = nums[0]

        for i in range(2,n+1):
            cache[i] = max(cache[i-1],cache[i-2]+nums[i-1])
        
        return cache[n]