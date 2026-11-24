class Solution {
    public int[] productExceptSelf(int[] nums) {

        int arrLen = nums.length;
        int[] prefix = new int[arrLen];
        int[] suffix = new int[arrLen];
        int[] res = new int[arrLen];

        prefix[0] = 1;
        suffix[arrLen - 1] = 1;

        int acc = 1;

        for (int i = 1; i < arrLen; i++) {
            
            acc *= nums[i-1];
            prefix[i] = acc;

            // System.out.println(acc);
        }

        // System.out.println();
        acc = 1;

        for (int i = arrLen-2; i >= 0; i--) {
            
            acc *= nums[i+1];
            suffix[i] = acc;

            // System.out.println(acc);
        }

        for (int i = 0; i < arrLen; i++) {
            res[i] = suffix[i] * prefix[i];
        }

        return res;
    }
}