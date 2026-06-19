class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        l = len(nums)

        left = [1] * l
        right = [1] * l

        val = 1
        for i in range(1, l):
            val *= nums[i-1]
            left[i] = val
        
        print(left)
        
        val = 1
        for i in range(l, 1, -1):
            val *= nums[i-1]
            right[i-2] = val
        
        print(right)

        for i in range(l):
            res.append(left[i] * right[i])
        return res