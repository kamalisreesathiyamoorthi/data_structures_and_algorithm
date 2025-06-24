class Graph :
    
    def __init__(self) :
        self.adj_dict = {}
        
    def add_vertex (self , vertex) :
        if vertex not in self.adj_dict :
            self.adj_dict[vertex] = []
            
    def add_edge(self , v1 , v2 ) : # bi-directional edge
        if v1 in self.adj_dict and v2 in self.adj_dict :
            self.adj_dict[v1].append(v2)
            self.adj_dict[v2].append(v1)
        
    def remove_edge(self , v1 , v2) : #removing the edge between the vertices v1 and v2
        if v1 in self.adj_dict and v2 in self.adj_dict :
            try :
                self.adj_dict[v1].remove(v2)
                self.adj_dict[v2].remove(v1)
            except ValueError :
                pass
        
    def remove_vertex (self , vertex) :
        if vertex in self.adj_dict :
            for related_vertex in self.adj_dict[vertex] :
                self.adj_dict[related_vertex].remove(vertex)
            del self.adj_dict[vertex]
            
            
    def print_graph(self) :
        for vertex in self.adj_dict :
            print(f"{vertex} -> {self.adj_dict[vertex]}")

            
            
my_graph = Graph() 
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A" , "B")
my_graph.add_edge("A" , "C")
my_graph.add_edge("A" , "D")
my_graph.add_edge("B" , "C")
my_graph.add_edge("B" , "D")
my_graph.add_edge("C" , "D")

my_graph.print_graph()
'''
A -> ['B', 'C', 'D']
B -> ['A', 'C', 'D']
C -> ['A', 'B', 'D']
D -> ['A', 'B', 'C']
'''

my_graph.remove_edge("A" , "D")

my_graph.print_graph()
'''
A -> ['B', 'C']
B -> ['A', 'C', 'D']
C -> ['A', 'B', 'D']
D -> ['B', 'C']
'''

my_graph.remove_vertex("A")

my_graph.print_graph()

'''
B -> ['C', 'D']
C -> ['B', 'D']
D -> ['B', 'C']
'''