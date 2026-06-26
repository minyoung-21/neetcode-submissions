class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.ht = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, key: int, value: int) -> None:
        # save current last node
        prev_node = self.tail.prev 
        # new node at tail
        self.tail.prev = Node(key, value) 
        new_node = self.tail.prev
        new_node.prev = prev_node
        new_node.next = self.tail
        # connect saved last node to new node
        prev_node.next = new_node
        # update ht
        self.ht[key] = new_node
        # update count
        self.count += 1
    
    def remove(self, key: int) -> None:
        # node we want to delete
        curr_node = self.ht[key]
        # next node of the node we want to delete
        next_node = curr_node.next
        # prev node of the node we want to delete
        prev_node = curr_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.ht[key]
        self.count -= 1
        

    def get(self, key: int) -> int:

        if key in self.ht.keys():
            value = self.ht[key].val
            self.remove(key)
            self.insert(key, value)
            return self.ht[key].val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.ht.keys():
            # update the val instead of adding a new one
            self.remove(key)
            
        if self.count >= self.cap:
            # delete the head.next
            self.remove(self.head.next.key)
        self.insert(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)