
# 🌳 Tree Traversal in Data Structures
Tree traversal refers to the process of visiting each node in a tree data structure **exactly once** in a systematic way. It is essential for operations like searching, printing, or modifying data in a tree.

## 📂 Types of Tree Traversal
Tree traversal is generally classified into two categories:

### 1. Depth-First Traversal (DFT)
This explores as far as possible along each branch before backtracking.

There are three common types of depth-first traversals:

🔹 **a. Inorder Traversal (Left, Root, Right)**
- Visit the left subtree
- Visit the root node
- Visit the right subtree

Used for: Binary Search Trees to get nodes in ascending order.

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
```

🔹 **b. Preorder Traversal (Root, Left, Right)**
- Visit the root node
- Visit the left subtree
- Visit the right subtree

Used for: Copying the tree, prefix expression.

```python
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
```

🔹 **c. Postorder Traversal (Left, Right, Root)**
- Visit the left subtree
- Visit the right subtree
- Visit the root node

Used for: Deleting the tree, postfix expression.

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
```

---

### 2. Breadth-First Traversal (BFT) or Level Order
This explores all nodes at the present depth level before moving to nodes at the next level.

Used for: Shortest path algorithms, serialization.

```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 🧠 Example Tree

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

| Traversal Type | Output       |
|----------------|--------------|
| Inorder        | 4 2 5 1 3 6  |
| Preorder       | 1 2 4 5 3 6  |
| Postorder      | 4 5 2 6 3 1  |
| Level Order    | 1 2 3 4 5 6  |

---

## 🔁 DFS vs BFS Comparison

| Feature            | DFS (Depth First Search)                   | BFS (Breadth First Search)                            |
|--------------------|--------------------------------------------|--------------------------------------------------------|
| **Traversal**      | Explores as far as possible along a branch | Explores all neighbors level by level                  |
| **Data Structure** | Stack (or recursion)                       | Queue                                                  |
| **Memory Usage**   | Less (if graph is shallow)                 | More (due to storing all neighbors)                    |
| **Path Finding**   | May not find the shortest path             | Always finds the shortest path (in unweighted graphs)  |
| **Usage**          | Better for solving puzzles, backtracking   | Better for shortest path, level-order traversal        |