# 📚 Data Structures in Python: Stack, Queue, and Deque

---

## 🔹 1. Stack (LIFO - Last In, First Out)
A stack is a linear data structure that follows the Last In First Out (LIFO) principle — the last element added is the first to be removed.

### Common Operations:
- push(item) – Add item to top
- pop() – Remove item from top
- peek() – View top item without removing

### 🧪 Example : Using queue.LifoQueue
```python
from queue import LifoQueue 

s = LifoQueue()
s.put(1)
s.put(2)
s.put(10)
s.put(5)
print(f"Stack : {s.get()}") #Stack : 5
print(f"Stack : {s.get()}") #Stack : 10
```
---

## 🔸 2. Queue (FIFO - First In, First Out)
A queue is a linear data structure that follows the First In First Out (FIFO) principle — the first element added is the first to be removed.

### Common Operations:
- enqueue(item) – Add item to rear
- dequeue() – Remove item from front

### 🧪Example : Using queue.Queue
```python
from queue import Queue

q = Queue()
q.put(1)
q.put(2)
q.put(10)
q.put(5)
print(f"Queue : {q.get()}") #Queue : 1
print(f"Queue : {q.get()}") #Queue : 2
```
---

## 🔹 3. Deque (Double-Ended Queue)
A deque supports insertion and deletion from both ends — front and rear.

### Common Operations:
- append(item) – Add to right
- appendleft(item) – Add to left
- pop() – Remove from right
- popleft() – Remove from left

### 🧪Example : Using collections.deque
```python
from collections import deque

d = deque()
d.append(1)
d.appendleft(12)
print(d) #deque([12, 1])
print(f"Queue : popleft : {d.popleft()}") #Queue : popleft : 12
print(f"Queue : popright: {d.pop()}") #Queue : popright: 1
```
---
