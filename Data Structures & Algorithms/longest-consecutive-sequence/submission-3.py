class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort();
        hs = set();
        count_arr = [];
        count = 0;

        for i in range(len(nums)):
            hs.add(nums[i]);
            if i == 0:
                count = 1;
            elif nums[i] - nums[i-1] == 1:
                count += 1;
            elif nums[i] - nums[i-1] > 1:
                count_arr.append(count)
                
                count = 1;
        
        count_arr.append(count)
        count_arr.sort();
        print(count_arr)
        print(hs)

        return count_arr[len(count_arr)-1];