class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        # how many prereq does each course i have?
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0

        while q:
            start = q.popleft()
            finish += 1

            for req in adj[start]:
                indegree[req] -= 1
                if indegree[req] == 0:
                    q.append(req)
        print(finish, numCourses)
        return finish == numCourses