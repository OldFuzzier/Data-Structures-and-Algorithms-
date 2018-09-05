#
# coding=utf-8

# 706 Design a HashMap

class ListNode(object):
    
    def __init__(self, key, value):
        self.k = key
        self.val = value
        self.next = None

# PCway: 链地址法 通过取余进行hash, 用链表解决了Collisions
class MyHashMap(object):

    def __init__(self):
        self.size = 10000  # hash szie
        self.bucket = [0 for _ in xrange(self.size)]

    def put(self, key, value):
        index = self.hash(key)
        if not self.bucket[index]:  # this index is Null
            self.bucket[index] = ListNode(-1, -1)  # Treickier: new dummy
        pre_node = self.find_node(key, index)
        if not pre_node.next:  # pre_node is the last node
            pre_node.next = ListNode(key, value)
            return  # break
        pre_node.next.val = value  # update ListNode

    def get(self, key):
        index = self.hash(key)
        if not self.bucket[index]:  # self.bucket[index] == 0
            return -1
        pre_node = self.find_node(key, index)
        return pre_node.next.val if pre_node.next else -1

    def remove(self, key):
        index = self.hash(key)
        if not self.bucket[index]: return  # break
        pre_node = self.find_node(key, index)
        pre_node.next = pre_node.next.next if pre_node.next else None  # ListNode Trickier

    def hash(self, key):
        return key % self.size

    def find_node(self, key, index):
        pre_node = self.bucket[index]
        node = pre_node.next
        while node and node.k != key:
            pre_node = node
            node = pre_node.next
        return pre_node


# Myway, size过大 then no accept
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1]*1000000
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.arr[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.arr[key]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.arr[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
