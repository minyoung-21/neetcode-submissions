class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num = len(prerequisites)
        ht = {i:[] for i in range(numCourses)}

        visited = set()
        finished = set()

        for j in range(num):
            ht[prerequisites[j][0]].append(prerequisites[j][1])

        def dfs(course) -> bool:
            if course in finished:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for req in ht[course]:

                if not dfs(req):
                    return False
            
            visited.remove(course)
            finished.add(course)
            return True

        
        for k in ht.keys():
            if not dfs(k):
                return False
        
        return True