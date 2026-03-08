class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = [0]*numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] +=1

            
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for n in graph[node]:
                indegrees[n]-=1
                if indegrees[n]==0:
                    q.append(n)
        return all(indegree == 0 for indegree in indegrees)




        