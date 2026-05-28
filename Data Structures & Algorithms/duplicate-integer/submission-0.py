class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myList = [];
        for x in nums:
            if x in myList:
                return True;
            else:
                myList.append(x);

        return False;