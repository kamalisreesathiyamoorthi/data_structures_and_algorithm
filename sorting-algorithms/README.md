# 📘 Sorting Algorithms in Data Structures

✅ **What is Sorting?**  
Sorting is the process of arranging data in a specific order — typically ascending or descending.  
It’s essential for tasks like searching, reporting, and organizing data.

---

## 📊 Common Sorting Algorithms

### 1. Bubble Sort
- Repeatedly compares adjacent elements and swaps them if they're in the wrong order.  
- **Time Complexity:** O(n²)  
- **Space:** O(1)  
- **Stable:** ✅  
- **Best Use:** Educational purposes or very small datasets.

### 2. Selection Sort
- Finds the minimum element and places it at the beginning. Repeats for the rest.  
- **Time Complexity:** O(n²)  
- **Space:** O(1)  
- **Stable:** ❌  
- **Best Use:** When memory is very limited.

### 3. Insertion Sort
- Builds the sorted list one element at a time by inserting elements in their correct position.  
- **Time Complexity:** O(n²)  
- **Space:** O(1)  
- **Stable:** ✅  
- **Best Use:** Small or nearly sorted datasets.

### 4. Merge Sort
- Divide and conquer algorithm that splits the array, sorts each part, then merges them.  
- **Time Complexity:** O(n log n)  
- **Space:** O(n)  
- **Stable:** ✅  
- **Best Use:** Large datasets or linked lists.

### 5. Quick Sort
- Uses a pivot to partition the array, then sorts partitions recursively.  
- **Time Complexity:** O(n log n) average, O(n²) worst  
- **Space:** O(log n)  
- **Stable:** ❌  
- **Best Use:** Very fast for most real-world data.

### 6. Heap Sort
- Builds a max heap, repeatedly swaps root with last element, and heapifies.  
- **Time:** O(n log n)  
- **Space:** O(1)  
- **Stable:** ❌  
- **Best Use:** When constant space is important and worst-case performance must be good.

---

## 📌 Comparison Table

| Algorithm          | Best Case  | Average Case | Worst Case | Space    | Stable | Notes                         |
|--------------------|------------|--------------|------------|----------|--------|-------------------------------|
| **Bubble Sort**    | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅      | Best case when already sorted |
| **Selection Sort** | O(n²)      | O(n²)        | O(n²)      | O(1)     | ❌      | Fewest swaps                  |
| **Insertion Sort** | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅      | Good for nearly sorted arrays |
| **Merge Sort**     | O(n log n) | O(n log n)   | O(n log n) | O(n)     | ✅      | Guaranteed performance        |
| **Quick Sort**     | O(n log n) | O(n log n)   | O(n²)      | O(log n) | ❌      | Fast in practice              |
| **Heap Sort**      | O(n log n) | O(n log n)   | O(n log n) | O(1)     | ❌      | Good worst-case guarantee     |