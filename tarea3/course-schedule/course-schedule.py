from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        courses_taken = 0
        while queue:
            current = queue.popleft()
            courses_taken += 1
            
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return courses_taken == numCourses