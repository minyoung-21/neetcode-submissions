class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                ind, t = stack.pop()
                res[ind] = i - ind
                # print(stack)
            stack.append([i, temp])
        return res