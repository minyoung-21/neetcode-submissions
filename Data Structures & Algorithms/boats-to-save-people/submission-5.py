class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        arr = [0] * m
        i = idx = boat = 0
        
        for w in people:
            arr[w-1] += 1

        for idx in range(len(people)):
            while arr[i] == 0:
                i += 1
            # counting sort!
            # position i means the value
            # because we made a frequency array that increases by 1
            # when there is a number in the people array that equals i
            people[idx] = i+1
            arr[i] -= 1
        
        # things are sorted
        # use limit - max = remainder
        # increment if the min weight can join the boat

        l, r = 0, len(people)-1
        while l <= r:
            remainder = limit - people[r]
            boat += 1
            r -= 1
            if remainder >= people[l]:
                l += 1

        return boat