class Solution:
    def maxArea(self, heights: List[int]) -> int:
        temp = 0;
        l = 0
        r = len(heights)-1;
        while l < r:
            
            area = (r-l) * min(heights[r], heights[l]);
            temp = max(temp, area)

            if heights[r] < heights[l]:
                r -= 1
            elif heights[r] >= heights[l]:
                l += 1;
        return temp