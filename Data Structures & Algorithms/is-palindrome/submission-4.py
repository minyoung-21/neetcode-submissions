class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0;
        r = len(s) - 1;

        while l < r:
            # if s[i].isalnum() == True and s[j].isalnum == True:
            #     print(s[i])
            #     print(s[j])
            #     if s[i].lower() == s[j].lower():
            #         i += 1;
            #         j -= 1;
            #     else:
            #         return False
            
            while s[l].isalnum() == False and l < r:
                l += 1;
            
            while s[r].isalnum() == False and l<r:
                r -= 1;
            
            print(s[l])
            print(s[r])
            while s[l].lower() != s[r].lower():
                return False;
            
            l += 1;
            r -= 1;
            
        return True












