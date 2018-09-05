#
# coding=utf-8

# 705 Design a Hash Table
# !: self.pos[key]中是key不能为index

# Myway: 取余hash+array解决confliction
class MyHashSet(object):

    def __init__(self):
        self.size = 1001  # 0-1000000
        self.buckets = [False for _ in xrange(self.size)]
        
    def add(self, key):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = []  # new a array
        i = self.find(key, index)
        if i != -1:  # 如果array中存在key，需要先删除
            self.buckets[index].pop(i)
        self.buckets[index].append(key)  # insert
        
    def remove(self, key):
        index = self.hash(key)
        # if not self.buckets[index]: return  # break
        i = self.find(key, index)  # 找到array位置
        if self.buckets[index] and i != -1:  # Trickier written
            self.buckets[index].pop(i)
        
    def contains(self, key):
        index = self.hash(key)
        if self.buckets[index] and self.find(key, index) != -1:
            return True
        return False
    
    def hash(self, key):
        return key % self.size
    
    def find(self, key, index):
        """查询key是否在array中"""
        if self.buckets[index]:
            for i in xrange(len(self.buckets[index])):
                if self.buckets[index][i] == key:
                    return i
        return -1

    
# PCway: 取余hash+array解决confliction, array position: key/size
# 完全实现了 O(1)
class MyHashSet(object):

    def __init__(self):
        self.size = 1001  # 0-1000000
        self.buckets = [False for _ in xrange(self.size)]
        
    def add(self, key):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = [False for _ in xrange(self.size)]
        self.buckets[index][self.pos(key)] = True  # index_son=self.hash(key)
        
    def remove(self, key):
        index = self.hash(key)
        if self.buckets[index]:
            self.buckets[index][self.pos(key)] = False
        
    def contains(self, key):
        index = self.hash(key)
        # if not self.buckets[index]: return False
        return self.buckets[index] and self.buckets[index][self.pos(key)]  # Trickier Written
    
    def hash(self, key):
        return key % self.size
    
    def pos(self, key):
        return  key / self.size
        

# PCway size over, then no accept
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False]*1000000
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = False
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.arr[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
