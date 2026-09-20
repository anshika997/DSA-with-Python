class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else:
            return False

# Object create
obj = MyHashSet()

# Add elements
obj.add(1)
obj.add(2)
obj.add(2)   # duplicate, add nahi hoga

print(obj.data)

# Check elements
print(obj.contains(1))
print(obj.contains(3))

# Remove element
obj.remove(2)

print(obj.data)
print(obj.contains(2))