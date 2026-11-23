class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> hm = new HashMap<>();
        // List<List<String>> res = new ArrayList<>();

        for (String s : strs) {
            int[] count = new int[26];
            for (int i = 0; i < s.length(); i++){
                // hm.put(s.charAt(i), hm.getOrDefault(s.charAt(i), 0) + 1);

                count[s.charAt(i) - 'a'] += 1;
            }

            String temp = Arrays.toString(count);

            if (!hm.containsKey(temp)){
                hm.put(temp, new ArrayList<>(List.of(s)));
            }else{
                hm.get(temp).add(s);
            }
        }

        List<List<String>> res = new ArrayList<>(hm.values());
        

        // System.out.println(allVal);

        return res;
    }
}
