class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = {};
        res = [];
        for x in range(len(nums)):
            # try:
            #     a = nums[x+1:].index(target - nums[x]);
            # except ValueError:
            #     continue;
            # if a+1 != x:
            #     res.append(x);
            #     res.append(a+1);
            
            if target - nums[x] in myList.keys():
                res.append(nums.index(target - nums[x]));
                res.append(x);
            myList[nums[x]] = target - nums[x];
        # for key in myList:
        #     if key in myList.values():
        #         print(key);
        return res;
