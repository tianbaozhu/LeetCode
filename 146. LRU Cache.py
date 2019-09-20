# Definition for doubly-linked list.
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.dummy_H = ListNode(0, 0)
        self.dummy_T = ListNode(0, 0)
        self.dummy_H.next = self.dummy_T
        self.dummy_T.prev = self.dummy_H
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            # move to tail
            Node = self.dict[key]
            Node.prev.next = Node.next
            Node.next.prev = Node.prev
            self.dummy_T.prev.next = Node
            Node.prev = self.dummy_T.prev
            self.dummy_T.prev = Node
            Node.next = self.dummy_T
            return Node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            Node = self.dict[key]
            Node.prev.next = Node.next
            Node.next.prev = Node.prev
            self.dummy_T.prev.next = Node
            Node.prev = self.dummy_T.prev
            self.dummy_T.prev = Node
            Node.next = self.dummy_T
            Node.val = value
            self.dict[key] = Node
        else:
            if self.capacity > len(self.dict):
                Node = ListNode(key, value)
                self.dummy_T.prev.next = Node
                Node.prev = self.dummy_T.prev
                self.dummy_T.prev = Node
                Node.next = self.dummy_T
                self.dict[key] = Node
            else:
                evict = self.dummy_H.next
                del self.dict[evict.key]
                self.dummy_H.next = evict.next
                evict.next.prev = self.dummy_H

                Node = ListNode(key, value)
                self.dummy_T.prev.next = Node
                Node.prev = self.dummy_T.prev
                self.dummy_T.prev = Node
                Node.next = self.dummy_T
                self.dict[key] = Node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
