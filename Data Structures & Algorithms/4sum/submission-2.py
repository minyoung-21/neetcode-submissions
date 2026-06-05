class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = 0;
        r = len(nums) - 1
        res = []
        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            
            if i > 0 and n == nums[i-1]:
                continue;

            for j in range(len(nums) - 1, -1, -1):
                
                if j < len(nums) - 1 and nums[j] == nums[j+1]:
                    continue;

                l = i + 1;
                r = j - 1;

                while l < r:

                    if n + nums[j] + nums[l] + nums[r] == target:
                        res.append([n, nums[j], nums[l], nums[r]])
                        
                        l += 1;
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif n + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                        
                    elif n + nums[j] + nums[l] + nums[r] < target:
                        l += 1
    
        return res;