class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [];
        l = 0;
        r = len(numbers) - 1;

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1;
            elif numbers[l] + numbers[r] < target:
                l += 1;
            else:
                res.append(l+1);
                res.append(r+1);
                return res