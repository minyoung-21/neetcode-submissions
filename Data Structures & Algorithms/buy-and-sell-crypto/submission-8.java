class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;

        int len = prices.length;
        int profit = 0;

        // b=buy, k=keep, s=sell
        // prices   = [10,1,5,6,7,1]
        // decision =  bb,k,k,k,k,s
        // decision =  bb,s,b,

        while (right < len) {
            if (prices[left] < prices[right]) {
                // we can keep or sell
                // keep
                // sell
                profit = Math.max(profit, prices[right] - prices[left]);
                // left = right;
                // right += 1;
            } else {
                // must not sell
                left = right;
            } 
            right += 1;
        }

        return profit;
    }
}
