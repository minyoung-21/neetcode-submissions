class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int containerSize = 0;

        while (left < right) {
            int h = Math.min(heights[left], heights[right]);
            containerSize = Math.max(containerSize, h * (right - left));

            if (heights[left] <= heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return containerSize;
    }
}
