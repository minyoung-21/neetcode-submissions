class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        int m = 0;

        while (l <= r) {
            m = l + (r - l) / 2;
            System.out.println(m);

            if (nums[m] == target) {
                return m;
            }

            if (nums[m] >= nums[l]) {
                // left is sorted
                if (target >= nums[l] && nums[m] > target) {
                    // move to left
                    r = m - 1;
                } else {
                    // move to right
                    l = m + 1;
                }
                
            } else {
                // check where target is
                // right is sorted
                if (nums[r] >= target && nums[m] < target) {
                    // target is not in right
                    l = m + 1;
                } else {
                    // target is 
                    r = m - 1;
                    
                }
            }
        }

        return -1;
    }
}
