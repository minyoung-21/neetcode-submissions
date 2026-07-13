class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = len(nums)

        def dfs(i:int, sub:List[int], cursum:int):
            if cursum == target:
                res.append(sub.copy())
            
            if cursum > target:
                return

            for j in range(i,l):
                sub.append(nums[j])
                dfs(j, sub, cursum+nums[j])
                sub.pop()
            
        dfs(0,[],0)

        return res