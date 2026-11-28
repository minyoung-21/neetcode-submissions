class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int l = 0;
        int r = 0;

        for (int w : weights) {
            l = Math.max(l, w);
            r += w;
        }

        int m = 0;
        int totalDays = 1;
        int res = r;

        while (l <= r) {
            m = l + (r - l) / 2;

            int currentLoad = 0;

            for (int w : weights) {
                if (currentLoad + w > m) {
                    totalDays += 1;
                    // put the package that didn't fit
                    // as the very first item
                    currentLoad = w;
                } else {
                    // it fits
                    currentLoad += w;
                }
            }

            if (days >= totalDays) {
                res = Math.min(res, m);
                r = m - 1;
                
            } else {
                l = m + 1;
            }
            totalDays = 1;

        }

        return res;
    }
}