class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];

        for (int n : nums) {
            count[n] += 1;
        }

        int index = 0;

        for (int i = 0; i < 3; i++) {
            
            while (count[i]-- > 0) {
                // System.out.println(i + "\t" + count[i]);
                nums[index++] = i;
            }
        }
    }
}