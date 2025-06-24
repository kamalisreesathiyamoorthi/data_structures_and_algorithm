
# 📘 Linked Lists in Data Structures

## 📌 What is a Linked List?
A Linked List is a linear data structure where each element (called a node) contains:

- **Data** – the actual value
- **Pointer/Reference** – to the next node in the sequence

Unlike arrays, linked lists do not store data contiguously in memory. Each node dynamically allocates memory and points to the next.

### ✅ Advantages
- Dynamic size (no fixed capacity)
- Efficient insertion/deletion at beginning/middle (O(1) for head/tail if reference is known)
- No memory wastage (unlike arrays with preallocated size)

### ❌ Disadvantages
- No random access (O(n) time to access nth element)
- Extra memory required for pointers
- Complexity in operations like reverse traversal or search

---

## 🔄 Types of Linked Lists

### 1. Singly Linked List
Each node points to the next node.  
The last node points to `None`.

```text
head → [data|next] → [data|next] → [data|next] → None
```

---

### 2. Doubly Linked List
Each node contains:

- `data`
- `prev` pointer to previous node
- `next` pointer to next node

```text
None ← [prev|data|next] ⇄ [prev|data|next] ⇄ [prev|data|next] ⇄ None
```

**Pros:**
- Bidirectional traversal
- Deletion is O(1) if pointer to node is given

**Cons:**
- More memory (2 pointers)
- Slightly more complex to manage

---

### 3. Circular Linked List
The last node points back to the head node (circular loop).

#### a. Singly Circular Linked List
```text
head → [data|next] → [data|next] → ... → [data|head]
```

#### b. Doubly Circular Linked List
```text
head ⇄ [prev|data|next] ⇄ ... ⇄ [prev|data|head]
```

**Use Cases:**
- Round-robin scheduling
- Continuous buffers

---

# 🔄 Time Complexity: Python List vs Linked List

| Operation         | Python List (Dynamic Array) | Linked List (Singly)     |
|------------------|-----------------------------|---------------------------|
| `append()`       | O(1)*                       | O(n) (need to traverse)   |
| `prepend()`      | O(n) (shift all elements)   | O(1)                      |
| `insert(i, x)`   | O(n) (shift elements)       | O(n) (traverse to index)  |
| `pop()` (last)   | O(1)                        | O(n) (traverse to end)    |
| `pop(0)`         | O(n) (shift all elements)   | O(1)                      |
| `remove(value)`  | O(n)                        | O(n)                      |
| `access(index)`  | O(1)                        | O(n)                      |
| `access(value)`  | O(n)                        | O(n)                      |

> *Python’s `list.append()` is **amortized O(1)** because resizing only occurs occasionally.

---

## ✅ When to Use What?

- **Use Python List**:
  - When you need **fast access by index**
  - When most operations happen at the **end**

- **Use Linked List**:
  - When doing frequent **insertions/deletions at the beginning**
  - When you don’t know the size in advance