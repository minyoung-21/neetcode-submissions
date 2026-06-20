class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        temp = []

        for carInd, carPos in enumerate(position):
            temp.append([carPos, speed[carInd]])
        
        temp.sort(reverse = True)
        stack.append(temp[0])

        
        for s in temp:
            
            t = stack[-1]
            stack.append(s)
            if (target-s[0])/s[1] <= (target-t[0])/t[1]:

                stack.pop()

        return len(stack)