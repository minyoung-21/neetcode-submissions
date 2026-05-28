class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        oneList = list(s);
        twoList = list(t);

        oneList.sort();
        twoList.sort();
        
        if oneList == twoList:
            return True;

        return False;