# -*- coding:utf-8 -*-


def parttion(nums, low, high):
    key = nums[low]
    while low < high:
        while low < high and nums[high] > key:
            high -= 1
        if low < high:  # 当出现<key的情况
            nums[low], nums[high] = nums[high], nums[low]  # 交换key和<key的元素
        else:
            break
        while low < high and nums[low] <= key:
            low += 1
        if low < high:  # 当出现>key的情况
            nums[high], nums[low] = nums[low], nums[high]  # 交换key和>key的元素
        else:
            break
    return low  # 此时 low==high

def easy_quick_sort(nums, low, high):
    if low < high:
        key_index = parttion(nums, low, high)
        easy_quick_sort(nums, low, key_index-1)
        easy_quick_sort(nums, key_index+1, high)



nums = [6, 4, 2, 1, 3]
easy_quick_sort(nums, 0, len(nums)-1)
print nums
