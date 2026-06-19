class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        count = 0
        for i, n in enumerate(temperatures):
            if not stack:
                stack.append([i, n])
            else:
                count = 0
                while stack and stack[-1][1] < n: 
                    # curr is greater so pop
                    stackInd, stackT = stack.pop()
                    res[stackInd] = i - stackInd
                
                stack.append([i, n])
            
        return res