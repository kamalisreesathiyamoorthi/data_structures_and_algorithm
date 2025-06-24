
# 📘 Graphs in Data Structures

## ✅ What is a Graph?
A Graph is a non-linear data structure consisting of:
- **Nodes (vertices)**: Represent entities.
- **Edges**: Represent relationships or connections between nodes.

## 🌐 Types of Graphs

### 1. Based on Direction

| Type       | Description                     | Example             |
|------------|----------------------------------|---------------------|
| Undirected | Edges have no direction (A—B)   | Social network      |
| Directed   | Edges have direction (A → B)    | Course prerequisites |

### 2. Based on Weight

| Type        | Description                    |
|-------------|--------------------------------|
| Unweighted  | Edges are equal                |
| Weighted    | Edges have weights (e.g., cost, distance) |

### 3. Other Variants
- Cyclic vs Acyclic
- Connected vs Disconnected
- Sparse vs Dense

## 🛠️ Graph Representation

### 1. Adjacency List (Recommended)
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```
- **Space Complexity**: O(V + E)

### 2. Adjacency Matrix
```python
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 0 ]
D [ 0 1 0 0 ]
```
- **Space Complexity**: O(V²)

## 🚀 Common Graph Algorithms

| Algorithm               | Purpose                               |
|------------------------|----------------------------------------|
| **DFS (Depth-First)**   | Traverse deep before wide              |
| **BFS (Breadth-First)** | Traverse level-by-level                |
| **Topological Sort**    | Order tasks with dependencies          |
| **Dijkstra’s**          | Shortest path (weighted graphs)        |
| **Bellman-Ford**        | Shortest path (with negative weights)  |
| **Floyd-Warshall**      | All-pairs shortest paths               |
| **Prim’s / Kruskal’s**  | Minimum Spanning Tree                  |
| **Union-Find**          | Detect connected components/cycles     |

## 🔍 Applications of Graphs
- Maps & Navigation (Google Maps)
- Social Networks (Facebook, LinkedIn)
- Recommendation Systems
- Task Scheduling
- Compilers (Topological Sort)
- Web Crawling

## 🌳 Tree vs 🌐 Graph

| Feature                       | **Tree**                                        | **Graph**                                               |
|------------------------------|--------------------------------------------------|----------------------------------------------------------|
| **Structure Type**            | Hierarchical (parent → child)                   | Network (nodes connected arbitrarily)                   |
| **Cycles**                    | ❌ No cycles allowed                             | ✅ Cycles may exist                                     |
| **Connectedness**             | ✅ Always connected                              | ❌ May or may not be connected                          |
| **Edges**                     | Exactly `n - 1` for `n` nodes                   | Can have up to `n(n - 1)/2` edges (in undirected)       |
| **Direction**                 | Directed (root → children) or undirected (rare) | Can be directed or undirected                          |
| **Root Node**                 | ✅ Has a single root node                        | ❌ No root required                                     |
| **Parent/Child Relationship** | Clearly defined (one parent, multiple children) | Not defined                                             |
| **Traversal Techniques**      | DFS, BFS, Preorder, Inorder, Postorder          | DFS, BFS                                                |
| **Examples**                  | File systems, HTML DOM, Organization chart      | Social networks, Road maps, Web links                   |
| **Applications**              | Hierarchical data storage                       | General-purpose relationships and connectivity modeling |