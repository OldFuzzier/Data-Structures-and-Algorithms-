#
# coding=utf-8

# 297. Serialize and Deserialize Binary Tree
# 二叉树的序列化与反序列化


# MyWay
class Codec:
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))

    # BFS
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root] if root else []
        res = ''
        while queue:
            node = queue.pop(0)
            if node:
                res += '%d,' % node.val
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += 'N,'
        # print res[:-1]
        return res[:-1]  # delete a ","
        
    
    # Trickier: queue+queue 一个控制node，一个控制left，right
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        val = data_list.pop(0)
        if not val: return None  # like ['']
        root = TreeNode(int(val))
        queue = [root]
        while queue:
            node = queue.pop(0)
            left_val = data_list.pop(0)
            right_val = data_list.pop(0)
            if left_val != 'N':
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            if right_val != 'N':
                node.right = TreeNode(int(right_val))
                queue.append(node.right)
        return root


# PCWay:  结果其实不太对
# Trickier: preorder
class Codec2:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)  # 1 2 # # 3 4 # # 5 # #

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
