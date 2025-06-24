# 📘 Hash Tables in Data Structures

## ✅ What is a Hash Table?
A Hash Table (or Hash Map) is a data structure that stores key-value pairs.  
It allows fast insertion, deletion, and lookup — typically in **O(1)** time on average.

## ✅ What is Hashing?
Hashing is a technique to map data of any size to a fixed-size value, called a **hash code** (or hash value), usually using a mathematical function.  
It is mainly used in **hash tables**, **data indexing**, **encryption**, and **fast lookups**.

## 🔑 Key Concepts 
| Concept           | Explanation                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **Key**           | Unique identifier used to access the value                       |
| **Value**         | Data associated with the key                                     |
| **Hash Function** | Converts the key into an index in an internal array              |
| **Collision**     | When two keys hash to the same index                             |
| **Resolution**    | Technique to handle collisions (e.g., chaining, open addressing) |

## ⚔️ Collision Handling Techniques
| Feature                  | **Chaining**                           | **Open Addressing**                          |
| ------------------------ | -------------------------------------- | -------------------------------------------- |
|  **Idea**              | Use a list/linked list at each index   | Find next available slot in the array        |
|  **Structure**         | Array of lists                         | Single array only                            |
|  **Memory Usage**      | Extra memory for lists                 | No extra memory needed                       |
|  **Insertion**         | O(1) average                           | O(1) average (can degrade)                   |
|  **Search Time**       | O(1) avg, O(n) worst                   | O(1) avg, O(n) worst                         |
|  **Deletion**          | Easy — just remove from list           | Complex — may need special markers           |
|  **Clustering Issue**  | No                                     | Yes (especially with linear probing)         |
|  **Resize Complexity** | Easier                                 | More complex (need to rehash all elements)   |
|  **Best For**          | When memory is available               | When memory is limited                       |
|  **Common in**         | Java (LinkedList buckets), Python dict | Hash tables in low-level memory-limited apps |

## 🧠 Advantages
- Very fast access (average O(1))
- Efficient for large datasets

## ⚠️ Limitations
- Poor performance if hash function causes many collisions
- Not ordered (in regular hash maps)
- Size may need resizing (costly)

## 💡 Applications of Hashing
- Hash Tables/Maps
- Databases (indexing)
- Password storage
- Compilers (symbol tables)
- Cryptography (SHA, MD5)