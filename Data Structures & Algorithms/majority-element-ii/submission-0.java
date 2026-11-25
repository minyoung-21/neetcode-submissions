class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int freq = nums.length / 3;
        Map<Integer, Integer> hm = new HashMap<>();
        List<Integer> res = new ArrayList<>();


        for (int i = 0; i < nums.length; i++) {
            hm.put(nums[i], hm.getOrDefault(nums[i], 0) + 1);

            if (hm.get(nums[i]) == freq+1) {
                res.add(nums[i]);
            }
        }

        

        return res;


    }
}