class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        int[] arr = new int[2];

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            if(hm.containsKey(diff)){
                return new int[]{hm.get(diff), i};
            }else{
                hm.put(nums[i], i);
            }
        }

        return new int[] {0,0};
    }
}
