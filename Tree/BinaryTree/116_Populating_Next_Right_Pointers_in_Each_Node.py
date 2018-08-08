# /usr/bin/python2.7
# coding=utf-8

# 116. Populating Next Right Pointers in Each Node
# 每个节点的右向指针

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
                    
                    
# PCWay use ListNode dont need deque
# 画出链表树的比较容易看出, 比较难理解
class Solution1(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if not root: return None
        cur  = root  # current Node
        next_ = root.left  # first level (is cur next level)

        while cur.left :
            cur.left.next = cur.right  # left --> right
            if cur.next:  #　本层是否为最后的ListNode
                cur.right.next = cur.next.left  # current ListNode right --> next ListNode left
                cur = cur.next  # next ListNode
            else:
                cur = next_  # callback to current level
                next_ = cur.left  # next level

