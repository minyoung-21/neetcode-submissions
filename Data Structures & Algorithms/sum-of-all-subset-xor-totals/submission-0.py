class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def subset(i: int, cur: int) -> List[int]:
            if i == len(nums):
                self.ans += cur
                return self.ans
            
            subset(i+1, cur ^ nums[i])

            subset(i+1, cur)
        
        subset(0, 0)
        return self.ans