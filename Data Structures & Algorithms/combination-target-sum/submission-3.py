class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(i: int, s: List[int], cursum: int):
            if cursum == target:
                res.append(s.copy())
                return
            
            for j in range(i, len(nums)):
                if cursum + nums[j] > target:
                    return
                
                s.append(nums[j])
                bt(j, s, cursum + nums[j])
                s.pop()
            

        bt(0,[], 0)

        return res