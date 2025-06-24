
# 🌲 Trees in Data Structures

## 📘 What is a Tree?
A **Tree** is a non-linear, hierarchical data structure made up of **nodes**. It consists of:
- **Root** – The topmost node.
- **Edges** – Connect parent and child nodes.
- **Leaves** – Nodes with no children.
- **Subtree** – Any node and its descendants.

> Unlike arrays and linked lists, trees represent data in a hierarchy, not a sequence.

---

## 📂 Common Terminologies

| Term   | Description |
|--------|-------------|
| Node   | An element of the tree containing data. |
| Root   | The top node with no parent. |
| Child  | A node directly connected to another when moving away from the root. |
| Parent | A node that has one or more children. |
| Leaf   | A node with no children. |
| Edge   | A connection between two nodes. |
| Height | The number of edges on the longest path from the node to a leaf. |
| Depth  | The number of edges from the root to the node. |
| Subtree| A tree consisting of a node and its descendants. |

---

## 🌳 Types of Trees

### 1. Binary Tree
Each node has at most two children (left and right).

### 2. Binary Search Tree (BST)
A binary tree where:
- Left subtree values < root
- Right subtree values > root

### 3. AVL Tree
A self-balancing BST where the difference between heights of left and right subtrees is no more than 1.

### 4. Red-Black Tree
A self-balancing BST with color rules to ensure balance during insertions and deletions.

### 5. Heap
A complete binary tree where each node is:
- Greater (Max Heap)
- Smaller (Min Heap) than its children.

### 6. Trie (Prefix Tree)
A tree used for storing strings efficiently for searching prefixes (e.g., autocomplete).

---

## 🕒 Time Complexity Summary

| Operation | Balanced BST (e.g., AVL) | Skewed Tree | Heap     |
|-----------|---------------------------|-------------|----------|
| Insertion | O(log n)                  | O(n)        | O(log n) |
| Deletion  | O(log n)                  | O(n)        | O(log n) |
| Search    | O(log n)                  | O(n)        | O(n)     |

---

## 📦 Applications of Trees

- Storing hierarchical data (file systems, DOM trees)
- Databases (B-Trees, B+ Trees)
- Routing algorithms (Trie, Huffman coding)
- Syntax parsing (compilers)
- AI & games (decision trees, minimax)