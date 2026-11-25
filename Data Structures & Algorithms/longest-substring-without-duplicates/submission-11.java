class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();

        if (len <= 0) {
            return len;
        }

        int left = 0;
        // int right = 0;
        int maxCount = 0;

        Set<Character> seen = new HashSet<>();

        for (int right = 0; right < len; right++) {

            while (seen.contains(s.charAt(right))) {
                seen.remove(s.charAt(left));
                left += 1;
            }

            // System.out.print(right-left);
            seen.add(s.charAt(right));
            maxCount = Math.max(right-left+1, maxCount);
        }

        return maxCount;
    }
}
