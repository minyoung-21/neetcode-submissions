class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = []
        def dfs(i: int, cursum: int) -> List[int]:
            if i == len(nums) or cursum > target:
                # ran out of memory
                return
            if cursum == target:
                res.append(s.copy())
                return 
            else:
                s.append(nums[i])
                dfs(i, cursum+nums[i]) # continue

                s.pop()
                dfs(i+1, cursum) # skip
        
        dfs(0, 0)
        return res