# /usr/bin/python2.7
# coding=utf-8

# 117. Populating Next Right Pointers in Each Node II
# # 每个节点的右向指针二

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


# MyWay BFS+queue
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = [root] if root else []
        while queue:
            # print queue
            rootLink = None  # every level's head
            for _ in xrange(len(queue)):  # control level 
                root = queue.pop(0)
                if rootLink:
                    rootLink.next = root  # add LinkNode
                    rootLink = rootLink.next  # next pointer
                else:
                     # create first LinkNode
                    rootLink = root
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
                    
                    
# PCWay Trickier: prekid and kid to build LinkNode
class Solution1(object):
    def connect(self, root):
        # @param root, a tree link node
        # @return nothing
        prekid = kid = TreeLinkNode(0)  # Trickier: dummy
        while root:
            while root:  # 在这一层级实现 ListNode
                kid.next = root.left   # Trickier:  
                kid = kid.next or kid  # 相当于 if root.left: kid = root.left
                kid.next = root.right
                kid = kid.next or kid  # 相当于 if root.right: kid = root.right
                root = root.next
            root, kid = prekid.next, prekid  # next level from dummy

