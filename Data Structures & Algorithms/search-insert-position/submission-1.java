class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        int m = 0;
        int res = nums.length;

        while (l < r) {
            m = l + (r - l) / 2;
            // System.out.println(m);

            if (nums[m] > target) {
                r = m;
                res = m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                return m;
            }
        }

        return res;

    }
}