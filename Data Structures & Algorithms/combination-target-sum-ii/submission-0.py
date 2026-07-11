class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        

        def bfs(i: int, subset: List[int], cursum: int):
            
            if cursum == target:
                res.append(subset.copy())

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if cursum > target:
                    return 
                # print(subset)
                subset.append(candidates[j])
                bfs(j+1, subset, cursum+candidates[j])
                subset.pop()
        bfs(0, [], 0)
    
        return res