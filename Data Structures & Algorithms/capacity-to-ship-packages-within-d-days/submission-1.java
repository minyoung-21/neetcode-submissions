class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int l = 0;
        int r = 0;
        int m = 0;
        int res = Integer.MAX_VALUE;

        for (int w : weights) {
            l = Math.max(l, w);
            r += w;
        }

        while (l <= r) {
            m = l + (r-l) / 2;

            int totalWeight = 0;
            int totalDays = 1;

            for (int w : weights) {
                if (totalWeight + w > m) {

                    // we can't add
                    // we add another day
                    totalDays += 1;
                    totalWeight = w;
                } else {
                    // we can add 
                    totalWeight += w;
                }
            }

            if (totalDays > days) {
                // takes too much time
                // increase
                l = m + 1;
            } else {
                res = m;
                r = m - 1;
            }



        }
        return res;
    }
}