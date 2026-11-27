class Solution {
    public boolean search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int m = 0;

        while (l <= r) {
            m = l + (r - l) / 2;

            if (nums[m] == target) {
                return true;
            }

            // dup check
            if (nums[m] == nums[l] && nums[m] == nums[r]) {
                l++;
                r--;
                continue;
            }

            // left is sorted
            if (nums[m] > nums[l]) {
                // check if target is in there
                if (target == nums[l]) {
                    return true;
                }
                if (target > nums[l] && target < nums[m]) {
                    // target is in l-m range
                    // we check left
                    r = m - 1;
                } else {
                    // target is not in l-m range
                    l = m + 1;
                }

            } else {
                // right is sorted
                if (target == nums[r]) {
                    return true;
                }

                if (target > nums[m] && target < nums[r]) {
                    // target is in m-r range
                    // we check right
                    l = m + 1;
                    
                } else {
                    // target is not in m-r range
                    r = m - 1;
                }
            }
        }
        return false;
    }
}