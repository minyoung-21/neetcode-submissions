class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 0;
        int r = Arrays.stream(piles).max().getAsInt();
        int m = 0;
        int totalTime = 0;
        int res = 0;

        while (l <= r) {
            m = l + (r - l) / 2;

            for (int p : piles) {
                totalTime += Math.ceil((double) p/m);
            }

            if (totalTime <= h) {
                res = m;
                r = m - 1;
            } else {
                l = m + 1;
            }

            totalTime = 0;
        }

        return res;
    }
}
