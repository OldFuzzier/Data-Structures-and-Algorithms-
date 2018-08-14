#
# coding=utf-8

# Trickier: index属于(1, n)注意位置是1至n的索引
#           index/2位置的node一定是该node的father_node
#           index*2与index*2+1分别是node的child的左右index

# 自定义list, 为了实现自己的索引方式
class MyQueue(list):

    def __init__(self, lst=None):
        if not lst:
            self._lst = []
        else:
            self._lst = lst
            

    def __getitem__(self, i):
        return self._lst[i-1]

    def __setitem__(self, i, val):
        self._lst[i-1] = val

    def append(self, x):
        self._lst.append(x)
    
    def pop(self):
        return self._lst.pop()

    def __repr__(self):
        return str(self._lst)

    def __len__(self):
        return len(self._lst)
        
    

# 实现最小二叉堆
class MyHeap(object):

    def __init__(self, lst):
        self._que = MyQueue()
        self.heapfy(lst)

    def heapfy(self, lst):
        for ele in lst:
            self.push(ele)

    def shift_up(self, i):
        while i/2 >= 1:  # 不能up超过 root 节点位置
            if self._que[i] < self._que[i/2]:
                self.swap(i, i/2)  # father与node进行交换
                i = i/2  # index指向father_node位置
            else:  # 如果不需要shift就break
                break

    def shift_down(self, i):
        n = len(self._que)
        while i*2 <= n:  # 不能down过最后一层最右node
            i_left = i*2  # child_left index
            i_right = i_left+1  # child_right index
            # Trickier: 下面一行判断了i_right的node是否存在，同时也判断了左右child的node哪个更小
            if i_right <= n and self._que[i_right] < self._que[i_left]:
                i_exchange = i_right
            else:
                i_exchange = i_left
            if self._que[i_exchange] < self._que[i]:
                self.swap(i_exchange, i)
                i = i_exchange  # index指向child的index
            else:  # 如果不需要shift就break
                break

    # 每次都要在最后新建一个node然后上浮
    def push(self, x):
        self._que.append(x)  # 将新元素添加到最后一位
        i = len(self._que)
        self.shift_up(i)  # 上浮

    # Trickier: 根节点与尾节点进行互换，然后让根节点下沉即可
    # 每次都是从最top进行pop
    def pop(self):
        n = len(self._que)
        self.swap(1, n)  # top and last 进行交换
        val = self._que.pop()  # pop
        self.shift_down(1)  # 交换后下沉
        return val

    # exchange each other
    def swap(self, i, j):
        self._que[i], self._que[j] = self._que[j], self._que[i]

    def __repr__(self):
        return str(self._que)

if __name__ == '__main__':
    lst = [8, 5, 2, 9, 3, 7, 1, 4, 6]
    h = MyHeap(lst)
    print h
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()
