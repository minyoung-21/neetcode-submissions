class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr_one = [];
        arr_two = [];
        for c in s:
            if c.isalnum():
                arr_one.append(c.lower())
                arr_two.insert(0,c.lower())
        
        print(arr_one)
        print(arr_two)
        return arr_one == arr_two;