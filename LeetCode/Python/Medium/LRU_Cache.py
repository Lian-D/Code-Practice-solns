class Node(object):
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        # end product should look like [left] <-> [cache val] .... <-> [right]

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.right, self.left = Node(0,0), Node(0,0) #Dummy Nodes
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node): #Insert on left
        prev = self.right.prev
        curr = self.right
        # Connect node to neighbors # [right prev] <-> [Node] <-> [right] end goal
        prev.next = node  
        curr.prev = node
        # Connect neighbors to node
        node.next = curr
        node.prev = prev
    
    def delete(self, node):
        prev_node, next_node = node.prev, node.next #Grab the current nodes prev and next
        prev_node.next = next_node # remove the node from connection
        next_node.prev = prev_node # remove the node from connection
        
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.delete(node) # Remove said node
            self.insert(node) # Put said Node at the start
            return node.val
        else: 
            return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.delete(self.cache.get(key)) #if it exists delete the eky
            
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if (len(self.cache) > self.cap):
            remove = self.left.next # remove the next of left, because we keep these nodes always
            self.delete(remove)
            del self.cache[remove.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # returns 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # returns -1 (not found)
print(cache.get(3))    # returns 3
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # returns -1 (not found)
print(cache.get(3))    # returns 3
print(cache.get(4))    # returns 4