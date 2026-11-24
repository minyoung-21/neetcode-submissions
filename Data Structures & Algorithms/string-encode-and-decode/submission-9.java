class Solution {

    public String encode(List<String> strs) {

        StringBuilder temp = new StringBuilder();

        for (String s : strs) {
            temp.append(s.length()).append("#").append(s);
        }

        return temp.toString();
    }

    // 5#Hello5#World

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();

        int i = 0;

        while (i < str.length()) {
            String strLen = "";

            while (str.charAt(i) != '#') {
                strLen += str.charAt(i);
                i += 1;
            }

            int len = Integer.parseInt(strLen);
            String word = str.substring(i+1, i+len+1);
            i += len +1;

            res.add(word);

            // System.out.println(i);
        }

        return res;
    }
}
