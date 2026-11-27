class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        int m = 0;
        int res = nums[0];

        while (l <= r) {

            if (nums[l] < nums[r]) {
                // it is in an increasing order
                res = Math.min(res, nums[l]);
                break;
            }

            m = l + (r - l) / 2;
            res = Math.min(res, nums[m]);

            if (nums[m] < nums[l]) {
                // left is sorted
                // The sorted side has no break point inside it
                // Every number goes smoothly up from left to right
                // search right
                r = m - 1;
            } else {
                l = m + 1;
            }

        }
        return res;
    }
}
