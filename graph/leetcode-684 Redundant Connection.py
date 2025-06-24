'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]


Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
'''

class Solution(object):
    def findRedundantConnection(self, edges):
        # Since there will be only one cycle forming edge
        n = len(edges)

        # initially parent of all nodes (1-n) will be itself and all their rank is 1 
        parent = []
        for node in range(n+1) :
            parent.append(node)
        rank = [1] * (n+1)

        def find(n) :
            p = parent[n]
            # a root node will always a parent of its own
            while p!=parent[p] :
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union( n1 , n2 ) :
            # find the root parent of nodes n1 and n2 
            p1 = find(n1)
            p2 = find(n2)

            #if they both have the same root parent , then this edge will create a cycle
            if p1 == p2 :
                return False 

            # change the parent of the parent nodes with greater ranked parent
            if rank[p1] > rank[p2] :
                parent[p2] = p1
                rank[p1] = rank[p1] + rank[p2]
            else :
                parent[p1] = p2 
                rank[p2] = rank[p2] + rank[p1]
            return True
        
        for n1,n2 in edges :
            if not union(n1,n2) :
                return [n1,n2]
        


    