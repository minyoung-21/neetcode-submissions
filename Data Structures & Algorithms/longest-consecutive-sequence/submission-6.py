class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ct = 0
        
        if len(nums) == 0:
            return 0
        temp = nums[0]
        for n in nums:
            print(n, temp)
            if n - temp == 1:
                count += 1
                
            elif n - temp == 0:
                continue
            else:
                count = 0
            ct = max(ct, count)
            temp = n
            print(count)

        return ct+1