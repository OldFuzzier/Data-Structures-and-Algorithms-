#!/usr/bin/env python
#coding:utf-8

'''3 合并排序
基本思想:
获取两个已经排序的列表，然后将他们合并成一个列表，
我们先以非常小的列表开始，然后不断对它们进行合并，
直到最终剩下单个已排序列表为止。'''

def merge(left, right):
    """合并两个数组"""
    merged = []
    i, j = 0, 0  # i, j 分别作为left和right的下标
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst)/2
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left,right)

l = [3,2,1,6,4,5]
print mergesort(l)
