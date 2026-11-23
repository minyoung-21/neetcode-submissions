class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hm = new HashMap<>();

        // Wrong!
        // List<Integer> arr = ArrayList<>();

        // Correct
        List<int[]> arr = new ArrayList<>();

        for (int n : nums) {
            hm.put(n, 1 + hm.getOrDefault(n, 0));
        }

        System.out.println(hm);

        for(Map.Entry<Integer, Integer> entry : hm.entrySet()) {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        }

        arr.sort((a, b) -> b[0] - a[0]);

        int[] res = new int[k];
        for(int i = 0; i < k; i++){
            res[i] = arr.get(i)[1];
        }

        return res;
    }
}
