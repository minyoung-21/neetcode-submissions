class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int right = 0;

        int len = s.length();
        int res = 0;
        int maxFreq = 0;

        HashMap<Character, Integer> hm = new HashMap<>();

        while (right < len) {
            hm.put(s.charAt(right), 1 + hm.getOrDefault(s.charAt(right), 0));
            // s = "AAABABB" k = 1
            maxFreq = Math.max(maxFreq, hm.get(s.charAt(right)));

            while ((right-left+1) - maxFreq > k) {
                hm.put(s.charAt(left), hm.get(s.charAt(left)) - 1);
                left += 1;
                
            } 

            
            res = Math.max(res, right-left+1);
            right += 1;
        }

        return res;
    }
}
