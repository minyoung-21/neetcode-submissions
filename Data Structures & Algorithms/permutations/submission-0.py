class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        used = [False] * l

        def dfs(i: int, s: List[int]) -> List[int]:
            if len(s) == l:
                res.append(s.copy())
                return
            
            for j in range(l):
                if not used[j]:
                    s.append(nums[j])
                    used[j] = True

                    dfs(j+1, s)

                    
                    s.pop()
                    used[j] = False
        dfs(0,[])
        return res