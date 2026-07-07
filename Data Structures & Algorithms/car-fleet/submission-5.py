class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        by_pos = []
        stack = []

        for i, p in enumerate(position):
            by_pos.append([p, speed[i]])
        
        by_pos.sort(reverse = True)
        stack.append(by_pos[0])
        print(by_pos)

        for s in by_pos:
            t = stack[-1]
            stack.append(s)
            
            if ((target - s[0]) / s[1]) <= ((target - t[0]) / t[1]):
                stack.pop()
        
        return len(stack)