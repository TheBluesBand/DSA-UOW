class HashTable:
    def __init__(self, input_cap):
        self.capacity = input_cap
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, value):
        return value % (self.capacity)
    
    def insert(self, value):
        key = self.hash(value)

        head = self.buckets[key]

        # Check if key already exists
        while head:
            if head.value == value:
                head.value = value
                return
            head = head.next

        # If key doesn't exist, create a new node and insert it
        new_node = Node(key, value)
        new_node.next = self.buckets[key]
        self.buckets[key] = new_node



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None