class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # bfs

        ht = {i:[] for i in range(n)}
        visit = [False] * n
        res = 0

        for a,b in edges:
            ht[a].append(b)
            ht[b].append(a)
        
        def bfs(source):
            q = deque([source])
            visit[source] = True

            while q:
                # dosth
                n = q.popleft()
                for y in ht[n]:
                    if not visit[y]:
                        q.append(y)
                        visit[y] = True
        
        for k in range(n):
            if not visit[k]:
                bfs(k)
                res += 1
        return res