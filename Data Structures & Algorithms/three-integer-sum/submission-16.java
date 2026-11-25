class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        // -4 -1 -1 0 1 2
        // fix one number, run two pointers on the rest

        for (int i = 0; i < nums.length; i++) {

            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            left = i + 1;
            right = nums.length - 1;

            while (left < right) {
                int sum = nums[left] + nums[right] + nums[i];

                if (sum == 0) {
                    res.add(new ArrayList<>(List.of(nums[left], nums[right], nums[i])));
                    // duplicates are dangerous in this case
                    // we only need to move left for dup
                    // because old right + new left -> new combination
                    // old right + old left -> only need to move left
                    
                    left += 1;
                    right -= 1;

                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                } else if (sum > 0) {
                    right -= 1;
                } else {
                    left += 1;
                }

                
            }
        }

        return res;
    }
}
