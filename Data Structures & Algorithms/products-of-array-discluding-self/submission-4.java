class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] prefix = new int[len];
        prefix[0] = 1;
        int[] suffix = new int[len];
        suffix[len-1] = 1;
        int[] res = new int[len];

        for (int i = 1; i < len; i++) {
            // product of everything strictly before i
            prefix[i] = nums[i-1] * prefix[i-1];
        }

        for (int i = len-2; i >= 0; i--) {
            suffix[i] = nums[i+1] * suffix[i+1];
        }

        for (int i = 0; i < len; i++) {
            // System.out.println(suffix[i]);
            res[i] = prefix[i] * suffix[i];
        }

        return res;

    }
}  
