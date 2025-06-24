'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

'''


class Solution(object):
    def findOrder(self, n , prerequisites):
        # TOPOLOGICAL SORT 
        #have a prerequisite map for each n courses
        pre_map = {}

        for course in range(n) :
            pre_map[course] = []

        # fill the prequisites of ach courses
        for c1,c2 in prerequisites :
            pre_map[c1].append(c2) 

        visited = set()
        cycle = set()
        output = []

        def dfs (course) :
            #if the course is already in cycle , then a cycle is found , thus course can't be complated 
            if course in cycle :
                return False
            
            if course in visited :
                return True
            
            cycle.add(course) 
            #check if all its prerequisites can be completed 
            for pre in pre_map[course] :
                if not dfs(pre) :
                    return False
            #now all its prerequisites can be completed 
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(n) :
            if not dfs(course) :
                return []
        return output
        