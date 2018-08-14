#!/usr/bin/env python
#coding:utf-8

'1 选择排序法'
（1）
def selection_1(lst):
    for i in range(len(lst)):
        #1 找到最小元素
        min_index = i   
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i,lst.pop(min_index))
（2）
def swap(lst,i,j):
    lst[i],lst[j] = lst[j],lst[i]

def selection_1(lst):                                  
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        swap(lst, i, min_index)




