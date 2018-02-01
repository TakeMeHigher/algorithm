import random
from .timewrap import *
import copy
import sys


sys.setrecursionlimit(100000)

def partition(li, left, right):
    # ri = random.randint(left, right)
    # li[left], li[ri] = li[ri], li[left]
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if left < right:    # 至少有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    return _quick_sort(li, 0, len(li)-1)

@cal_time
def sys_sort(li):
    li.sort()

li = list(range(100000))
random.shuffle(li)


#sys_sort(li1)
quick_sort(li)


''''
快速排序：快
快排思路：
取一个元素p（第一个元素），使元素p归位；
列表被p分成两部分，左边都比p小，右边都比p大；
递归完成排序。
时间复杂度:一般为O(nlgn) 最坏情况为O(n2)
'''