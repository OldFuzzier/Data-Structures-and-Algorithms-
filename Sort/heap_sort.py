#
# coding=utf-8

# heap_sort图解: https://www.cnblogs.com/linjj/p/5260763.html

# 整体思路:
# 1 create heap:
#       方式一: 正常的shift_up方法  O(nlogn)
#       方式二: 通过非叶子节点的点进行全部shift_down, 使所有root变成heap，最后得到heap. O(n)
# 2 delete+adjust：
#       delete首元素然后与尾元素互换
#       将更换后的首元素进行shift_down的adjust
#       排除尾元素的部分进入delete循环


# 最大堆
class HeapSort(object):

    def swap(self, lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    def shift_down(self, lst, root_i, heap_size):
        # params: root_i, 当前node的index
        # params: heap_size, 当前heap的length
        while root_i*2 < heap_size:
            child_left = root_i*2
            child_right = root_i*2+1
            if child_right < heap_size and lst[child_right] > lst[child_left]: # 找出左右最大的child
                exchange_i = child_right
            else:
                exchange_i = child_left
            if lst[exchange_i] > lst[root_i]:  # if need to shift down
                self.swap(lst, exchange_i, root_i)
                root_i = exchange_i  # update i
            else:
                break

    def sort(self, lst):
        lst.insert(0, -1)  # Trickier: 第一个元素不用，站位
        
        # 1 create MaxHeap
        n = len(lst)-1  # lst length
        root_i = n/2  # 最后一个非叶子节点的位置 (画图理解)
        while lst[root_i] > 0:  # 非叶子节点上移, 上移到位置为root_i=1位置处
            self.shift_down(lst, root_i, n)  # 判断该叶子节点是否满足堆得性质，不满足则进行调整
            root_i -= 1  # 移动到上一个非叶子节点
        print lst
        # 2 delete(exchange) and adjust
        heap_size = n
        while heap_size > 1:  
            self.swap(lst, 1, heap_size)  # 首尾互换，也就是max被移到了序列的末尾
            self.shift_down(lst, 1, heap_size)  # 调整位置在首(1)的root
            heap_size -= 1  # 末尾不必排序，所以用索引排除

        lst.pop(0)  # 剔除站位元素
        print lst
        return lst


# Time complexity: O(nlogn)  create_heap=O(k<n), delete_adjust=O(nlogn)
# space comlexity: O(1)

if __name__ == '__main__':
    # HeapSort().sort([5, 1, 3, 7, 55, 2, 77, 4])
        
        

        
