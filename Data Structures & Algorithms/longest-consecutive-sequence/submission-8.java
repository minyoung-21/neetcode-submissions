class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> trace = new HashMap<>();
        int res = 0;

        for (int n : nums) {
            if (!trace.containsKey(n)) {

                trace.put(n, 1 + trace.getOrDefault(n-1, 0) + trace.getOrDefault(n+1, 0));
                trace.put(n - trace.getOrDefault(n-1, 0), trace.get(n));
                trace.put(n + trace.getOrDefault(n+1, 0), trace.get(n));

                res = Math.max(res, trace.get(n));
            }
        }

        return res;

    }
}
