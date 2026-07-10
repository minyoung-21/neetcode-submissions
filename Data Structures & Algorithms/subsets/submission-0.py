class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        s = []
        def makeArr(i: int) -> List[int]:

            if i == len(nums):
                # stop
                res.append(s.copy())
            else:
                s.append(nums[i])
                makeArr(i+1)

                s.pop()
                makeArr(i+1)
        
        
        makeArr(0)
        return res
    
    