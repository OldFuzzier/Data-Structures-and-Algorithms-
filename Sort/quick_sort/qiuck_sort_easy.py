def qsort(l):
    if len(l) < 2:
        return l
    low = qsort([lt for lt in l[1:] if lt < l[0]])
    high = qsort([gt for gt in l[1:] if gt > l[0]])
    return low + l[0:1] + high
    
x = [4,2,1,3,5,11, 7, 9, 8]
print qsort(x)
