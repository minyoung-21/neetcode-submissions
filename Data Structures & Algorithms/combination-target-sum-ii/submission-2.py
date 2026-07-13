class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        l = len(candidates)
        check = [False]*l

        def dfs(i:int, sub:List[int], cursum:int):
            if cursum == target:
                res.append(sub.copy())
            
            if cursum > target:
                return
            
            for j in range(i,l):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if not check[j]:
                    check[j] = True
                    sub.append(candidates[j])
                    dfs(j+1, sub, cursum+candidates[j])
                    check[j] = False
                    sub.pop()
        dfs(0,[],0)
        return res