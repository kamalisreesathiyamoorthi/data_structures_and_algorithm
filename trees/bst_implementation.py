class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def BFS(self, root):
        my_queue = []
        values = []

        my_queue.append(root)
        while len(my_queue) != 0:
            temp = my_queue.pop(0)
            values.append(temp.value)
            if temp.left:
                my_queue.append(temp.left)
            if temp.right:
                my_queue.append(temp.right)

        return values

    def in_order(self, root, values=None):  # LDR
        if values is None:
            values = []
        if root:
            self.in_order(root.left, values)
            values.append(root.value)
            self.in_order(root.right, values)
        return values

    def pre_order(self, root, values=None):  # DLR
        if values is None:
            values = []
        if root:
            values.append(root.value)
            self.pre_order(root.left, values)
            self.pre_order(root.right, values)
        return values

    def post_order(self, root, values=None):  # LRD
        if values is None:
            values = []
        if root:
            self.post_order(root.left, values)
            self.post_order(root.right, values)
            values.append(root.value)
        return values

    def contains(self, root, search_value):
        if root is None:
            return False
        if root.value == search_value:
            return True
        elif search_value < root.value:
            return self.contains(root.left, search_value)
        else:
            return self.contains(root.right, search_value)

# Building BST
bst = BST()
bst.root = bst.insert(bst.root, 38)
bst.root = bst.insert(bst.root, 19)
bst.root = bst.insert(bst.root, 69)
bst.root = bst.insert(bst.root, 12)
bst.root = bst.insert(bst.root, 24)
bst.root = bst.insert(bst.root, 59)
bst.root = bst.insert(bst.root, 96)

print(f"BST root : {bst.BFS(bst.root)}")               # BST root : [38, 19, 69, 12, 24, 59, 96]
print(f"Searching 90 : {bst.contains(bst.root, 90)}")  # Searching 90 : False
print(f"Searching 19 : {bst.contains(bst.root, 19)}")  # Searching 19 : True

# DFS Traversal
print(f"PREORDER DFS : {bst.pre_order(bst.root)}")     # PREORDER DFS : [38, 19, 12, 24, 69, 59, 96]
print(f"POSTORDER DFS : {bst.post_order(bst.root)}")   # POSTORDER DFS : [12, 24, 19, 59, 96, 69, 38]
print(f"INORDER DFS : {bst.in_order(bst.root)}")       # INORDER DFS : [12, 19, 24, 38, 59, 69, 96]

# BFS Traversal
print(f"BFS : {bst.BFS(bst.root)}")                    # BFS : [38, 19, 69, 12, 24, 59, 96]



'''
# Without using recursion :
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        
        tempNode = self.root
        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            else:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False
        
    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    def BFS(self):
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(currentNode)
        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values

    def DFSPreOrder(self):
        values = []
        def traverse(currentNode):
            values.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        return values

    def DFSPostOrder(self):
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            values.append(currentNode.value)
        traverse(self.root)
        return values

    def DFSInOrder(self):
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            values.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        return values


bst = BinarySearchTree()
bst.insert(38)
bst.insert(19)
bst.insert(69)
bst.insert(12)
bst.insert(24)
bst.insert(59)
bst.insert(96)

print(f"BFS Traversal : {bst.BFS()}")                # BFS Traversal : [38, 19, 69, 12, 24, 59, 96]
print(f"Searching 90 : {bst.contains(90)}")          # Searching 90 : False
print(f"Searching 19 : {bst.contains(19)}")          # Searching 19 : True

print(f"DFS Pre-Order : {bst.DFSPreOrder()}")        # DFS Pre-Order : [38, 19, 12, 24, 69, 59, 96]
print(f"DFS Post-Order : {bst.DFSPostOrder()}")      # DFS Post-Order : [12, 24, 19, 59, 96, 69, 38]
print(f"DFS In-Order : {bst.DFSInOrder()}")          # DFS In-Order : [12, 19, 24, 38, 59, 69, 96]

min_node = bst.minOfNode(bst.root)
print(f"Minimum Value : {min_node.value}")           # Minimum Value : 12

max_node = bst.maxOfNode(bst.root)
print(f"Maximum Value : {max_node.value}")           # Maximum Value : 96

'''