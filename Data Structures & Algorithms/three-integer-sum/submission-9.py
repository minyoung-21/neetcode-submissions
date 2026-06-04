class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort();
        res = []
        temp = 0;

        r = len(nums) - 1;
        l = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = (nums[i] + nums[l] + nums[r])
                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]]);
                    r -= 1;
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1;
                elif temp > 0:
                    r -= 1;
                elif temp < 0:
                    l += 1;

        print(nums)
        return res