class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        if not nums or nums[0] > 0:
            return res

        # print(nums)
        for ind, num in enumerate(nums):

            l = ind + 1
            r = len(nums) - 1
            # print(ind, num == nums[ind-1], num, nums[ind-1])
            if ind != 0 and num == nums[ind-1]:
                continue
                
            while l < r:
                # print(num, nums[l], nums[r])
                v = num + nums[l] + nums[r]
                if v < 0:
                    # temp = nums[l]
                    l += 1
                    # while l < r and temp == nums[l]:
                    #     l += 1
                elif v > 0:
                    # temp = nums[r]
                    r -= 1
                    # while l < r and temp == nums[r]:
                    #     r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    temp = nums[l]
                    l += 1
                    while l < r and temp == nums[l]:
                        l += 1
        return res