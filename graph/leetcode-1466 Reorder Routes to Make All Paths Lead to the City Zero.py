'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).


Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).


Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

'''


class Solution(object):
    def __init__(self) :
        self.changes = 0 

    def minReorder(self, n, connections):
        # start at city 0
        # recursively check its neighbours to the city 
        # count the outgoing edges

        edges = set()
        for a,b in connections :
            edges.add((a,b))
        
        neighbours = {}

        # each n city has neighbours
        for city in range(n) :
            neighbours[city] = []
        
        # add the neighbours of each city from the edges
        for a,b in edges :
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()

        def dfs (city) :
            for neighbour in neighbours[city] : # check if all its neighbour has edge to that city 
                if neighbour in visited : # if that city is already visited 
                    continue
                #check if this neighbour can reach city 0 
                if ( neighbour , city ) not in edges :
                    self.changes = self.changes + 1

                visited.add(neighbour)
                dfs(neighbour)


        visited.add(0)
        dfs(0)
        return self.changes
            



'''
tc : 5 * O(n)
1. Building edges
2. Initialize neighbours
3. Finding neighbours
4. DFS Traversal
5. visited set Operation   

sc : O(n) (due to stack space)
'''