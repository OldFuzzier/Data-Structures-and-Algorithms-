
def mySort(lst):
    for i in xrange(len(lst)):
        flag = False  # marked
        for j in xrange(i-1, -1, -1):
            if lst[i] < lst[j]:
                flag = True
                temp = j  # need to exchaged flag
            else:
                # bigger than all of [temp:-1,-1]
                break
        if flag:
            swap(lst, i, temp)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


lst = [2, 1, 4, 3, 5]
print lst
mySort(lst)
print lst
