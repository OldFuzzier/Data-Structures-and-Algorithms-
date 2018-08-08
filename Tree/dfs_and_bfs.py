# coding=utf-8

lst = [1, 2, [3, [4, 4.1, 4.2], [5, 6], 7], 8]


# more than a List
def bfs1(lst):
    deque = []
    deque.append(lst)
    while deque:
        temp = deque.pop(0)
        for i in temp:
            if isinstance(i, list):
                deque.append(i)
            else:
                print i


# Trickier: use len(deque) control travel (not use this Example)
def bfs2(lst):
    deque = [lst]
    while deque:
        for _ in xrange(len(deque)):  # Trickier: length = len(deque)
            temp = deque.pop(0)
            if isinstance(temp, list):
                deque.append(temp)
            else:
                print temp


'''
void dfs(int step)
{
    判断边界，如果到了边界当然直接返回啦
    尝试每一种可能结果for(i=0;i<n;i++)
    {
        处理当前步
        继续下一步dfs(step + 1)
    }
    返回
}
'''
def dfs(lst):
    temp = []
    for item in lst:
        if isinstance(item, list):
            dfs(item)
        else:
            temp.append(item)
    print temp
    for i in temp:
        print i


if __name__ == '__main__':
    dfs(lst)
