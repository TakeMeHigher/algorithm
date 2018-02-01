import random
from .timewrap import *

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        # i 表示趟数
        # 第 i 趟时： 无序区：(0，len(li) - i)
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

@cal_time
def bubble_sort_2(li):
    for i in range(len(li) - 1):
        # i 表示趟数
        # 第 i 趟时： 无序区：(0，len(li) - i)
        change = False
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                change = True
        if not change:
            return

li = list(range(10000))
# random.shuffle(li)
# print(li)
bubble_sort_2(li)
print(li)

'''
列表每两个相邻的数，如果前边的比后边的大，那么交换这两个数
时间复杂度O(n2)
'''