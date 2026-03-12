class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8) 
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)