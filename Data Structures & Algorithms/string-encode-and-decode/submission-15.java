class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();

        for (String str : strs) {
            res.append(str.length()).append("#").append(str);
        }

        // System.out.println(res.toString());

        return res.toString();
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> res = new ArrayList<>();

        while (i < str.length()) {
            int k = i;
            // System.out.println(i);


            while (str.charAt(k) != '#') {
                k += 1;
            }

            int len = Integer.parseInt(str.substring(i, k));
            int start = k + 1;
            int end = start + len;
            String word = str.substring(start, end);

            // System.out.println(word);
            res.add(word);
            i = end;

        }

        return res;
    }
}
