import random
from .timewrap import *

@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        # i 表示趟数，也表示无序区开始的位置
        min_loc = i   # 最小数的位置
        for j in range(i + 1, len(li) - 1):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


li = list(range(10000))
random.shuffle(li)
print(li)
select_sort(li)
print(li)


'''
一趟遍历记录最小的数，放到第一个位置；
再一趟遍历记录剩余列表中最小的数，继续放置；
时间复杂度：O(n2)
'''