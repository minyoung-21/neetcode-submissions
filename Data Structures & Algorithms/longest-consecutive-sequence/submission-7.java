class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();
        int res = 0;

        for (int n : nums){
            if (!hm.containsKey(n)) {
                hm.put(n, hm.getOrDefault(n-1, 0) + hm.getOrDefault(n+1, 0) + 1);
                // If you stand at num and step backward by the 
                // exact count of numbers to your left, 
                // you land on the first number in that group.

                // Only the two outer boundaries hold the 
                // true length of the chain, because those are 
                // the only two doors future numbers can ever knock on
                hm.put(n-hm.getOrDefault(n-1, 0), hm.get(n));
                hm.put(n+hm.getOrDefault(n+1, 0), hm.get(n));

                res = Math.max(res, hm.get(n));
            }
            
        }

        return res;
    }
}
