class Node:
    def __init__(self, value, priority):
        self.value = value 
        self.priority = priority  
        self.left = None  
        self.right = None  

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, current, new_node):
        if new_node.priority > current.priority:
            if current.left:
                self._insert_node(current.left, new_node)
            else:
                current.left = new_node
        else:
            if current.right:
                self._insert_node(current.right, new_node)
            else:
                current.right = new_node

    def _find_max_priority_node(self, current):
        if current is None:
            return None, None
        parent, node = None, current
        while node.left:
            parent = node
            node = node.left
        return parent, node

    def pop(self):
        if not self.root:
            return None
        parent, node = self._find_max_priority_node(self.root)
        if node == self.root:
            self.root = node.right
        elif parent:
            parent.left = node.right
        return node.value

    def peek(self):
        _, node = self._find_max_priority_node(self.root)
        return node.value if node else None

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append((node.value, node.priority))
            self._in_order(node.right, result)

    def view(self):
        result = []
        self._in_order(self.root, result)
        return result
    
pq = PriorityQueue()
pq.insert("A", 1)
pq.insert("B", 5)
pq.insert("C", 10)

print("Queue (in-order):", pq.view())
print("Highest priority (peek):", pq.peek())
print("Deleted (pop):", pq.pop())
print("Queue after deleted:", pq.view())


