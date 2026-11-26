class Solution {
    public String minWindow(String s, String t) {
        int left = 0;
        int right = 0;
        int minLen = Integer.MAX_VALUE;
        int resStart = 0;

        int slen = s.length();
        Map<Character, Integer> countS = new HashMap<>();

        int tlen = t.length();
        Map<Character, Integer> countT = new HashMap<>();
        
        for (int i = 0; i < tlen; i++) {
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        int need = countT.size();
        int have = 0;
        char ch = 'a';

        while (right < slen) {
            ch = s.charAt(right);
            countS.put(ch, countS.getOrDefault(ch, 0) + 1);

            if (countT.containsKey(ch) && countS.get(ch).intValue() == countT.get(ch).intValue()) {
                have += 1;
            }
            
            // System.out.println(have + "\t" + need + "\t" + ch);

            while (have == need) {
                // minLen = Math.min(right-left+1, minLen);

                // if smaller len found
                if (minLen > right-left+1) {
                    // update minLen and resEnd
                    minLen = right-left+1;
                    resStart = left;
                }

                ch = s.charAt(left);

                // delete char freq
                countS.put(ch, countS.get(ch) - 1);
                
                // if we deleted what was needed, decrement have
                if (countT.containsKey(ch) && countS.get(ch).intValue() < countT.get(ch).intValue()) {
                    have -= 1;
                }
                
                left += 1;
            }

            right += 1;
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(resStart, resStart+minLen);
    }
}
