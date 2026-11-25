class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length()-1;

        while (left < right) {
            // s.charAt() returns a primitive char
            // primitive types do not have methods like .lower()
            // so use the static Character.toLowerCase() method
            // System.out.println(s.charAt(left) + "\t" + s.charAt(right));

            while (left < right && !alphaNum(s.charAt(left))) {
                left += 1;
            }

            while (left < right && !alphaNum(s.charAt(right))) {
                right -= 1;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left += 1;
            right -= 1;
        }

        return true;
    }

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || c >= 'a' && c <='z' || c >= '0' && c <= '9');
    }
}
