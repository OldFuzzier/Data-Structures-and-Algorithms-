#!/usr/bin/python
# -*- coding: utf-8 -*-

'2 冒泡排序法'
def bubble_sort(lst):
    exchanged = True  # marked, bset situation is O(n)
    top = len(lst) - 1
    while exchanged:
        exchanged = False
        for i in range(top):
            if lst[i] > lst[i+1]:
                swap(lst,i,i+1)
                exchanged = True
        top -= 1
