class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0;
        mult = 1;
        pref = [];
        suff = [];
        res = [];
        for i in range(len(nums)-1):
            if i == 0:
                pref.append(1)
            mult *= nums[i];
            pref.append(mult)
        mult = 1
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                suff.append(1)
                break;
            mult *= nums[i]
            suff.insert(0,mult)
        
        for i in range(len(nums)):
            res.append(suff[i] * pref[i])
        return res;