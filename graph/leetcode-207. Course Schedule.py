'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.


Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

'''

class Solution(object):
    def canFinish(self, n , prerequisites):
        # DFS + MEMOIZATION                                             tc : O(n+p) (p-no of prerequisite pairs)        sc : O(n+p)(due to pre_map) + O(n) (due to visited) + O(n) (call stack)
        # have a prerequisite map for each courses
        pre_map = {}

        for course in range(n) :
            pre_map[course] = []

        #fill the prerequisites of each course from the list
        for c1,c2 in prerequisites :
            pre_map[c1].append(c2)

        visited = set()

        def dfs(course) :
            # if the course is already in the path , then a cycle is found and return False since that course can't be completed
            if course in visited :
                return False
            
            #if the course has no prerequisites , then no issues
            if pre_map[course] == [] :
                return True
            
            visited.add(course)
            #check if the prerequisites of that course can be completed
            for pre in pre_map[course] :
                if not dfs(pre) :
                    return False #even if one of the prerequisite can't be done , return false
                
            # now all is prerequisites of the course can be done , so remove from the path
            pre_map[course] = []
            visited.remove(course)
            return True

        
        #Check if each course can be completed separately
        for course in range(n) :
            if not dfs(course) :
                return False

        return True
        