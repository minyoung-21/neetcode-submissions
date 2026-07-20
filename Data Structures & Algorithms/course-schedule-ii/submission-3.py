class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        ht = {i:[] for i in range(numCourses)}
        res = []
        
        # dst is pre req for src
        for src, dst in prerequisites:
            ht[dst].append(src)
            indegree[src] += 1
        
        q = deque()
        for j in range(numCourses):
            if indegree[j] == 0:
                q.append(j)
            
        while q:
            s = q.popleft()
            res.append(s)

            for req in ht[s]:
                indegree[req] -= 1
                if indegree[req] == 0:
                    q.append(req)
        
        if len(res) != numCourses:
            return []

        return res