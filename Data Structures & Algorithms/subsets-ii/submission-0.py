class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sub = [], []
        nums.sort()

        def dfs(i:int) -> List[int]:
            res.append(sub.copy())
            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                
                sub.append(nums[j])
                
                dfs(j+1)
                
                sub.pop()
        
        dfs(0)
        return res