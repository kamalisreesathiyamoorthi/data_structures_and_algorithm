# Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)

print(f"First Node Value : {first_node.value}")                     # First Node Value : 10
print(f"Second Node Value : {second_node.value}")                   # Second Node Value : 20
print(f"Third Node Value : {third_node.value}")                     # Third Node Value : 30

first_node.nextNode = second_node
second_node.nextNode = third_node

print(f"first_node.nextNode.value : {first_node.nextNode.value}")                     # first_node.nextNode.value : 20
print(f"first_node.nextNode.nextNode.value : {first_node.nextNode.nextNode.value}")   # first_node.nextNode.nextNode.value : 30


# Doubly Linked List

class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

x = DoublyNode(10)
y = DoublyNode(20)
z = DoublyNode(30)

print(f" x value : {x.value}")       # x value : 10
print(f" y value : {y.value}")       # y value : 20
print(f" z value : {z.value}")       # z value : 30

x.nextNode = y
y.nextNode = z

z.prevNode = y
y.prevNode = x

print(x.nextNode.value)              # 20
print(z.prevNode.value)             # 20