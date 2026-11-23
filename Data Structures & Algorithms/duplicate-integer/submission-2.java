class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();

        for (int n : nums) {
            if (hm.containsKey(n)){
                return true;
            }else{
                hm.put(n, 0);
            }
        }

        return false;
    }
}