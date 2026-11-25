class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;

        // int[] prefix = new int[];
        // int[] suffix = new int[];

        int res = 0;
        int leftMax = height[left];
        int rightMax = height[right];

        while (left < right) {
            // Water at any position depends on the shorter wall 
            // between the left and right sides
            // if left wall is shorter, right wall doesn't help
            // that means we can safely move right wall and vice versa
            if (leftMax > rightMax) {
                right -= 1;
                rightMax = Math.max(rightMax, height[right]);
                res += rightMax - height[right];
            } else {
                left += 1;
                leftMax = Math.max(leftMax,  height[left]);
                res += leftMax - height[left];
            }
        }

        return res;
    }
}
