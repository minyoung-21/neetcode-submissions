class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int len = s.length();

        if (len <= 1) {
            return len;
        }

        int maxCount = 0;
        int left = 0;
        Set<Character> seen = new HashSet<>();

        for (int right = 0; right < len; right++) {
            while (seen.contains(s.charAt(right))) {
                seen.remove(s.charAt(left));
                left += 1;
            }

            seen.add(s.charAt(right));
            maxCount = Math.max(maxCount, right-left+1);
        }

        return maxCount;
    }
}
