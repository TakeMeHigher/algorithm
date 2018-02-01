import random
from timewrap import *
import copy
import sys


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def _merge_sort(li, low, high):
    if low < high:  # 至少两个元素
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
        print(li[low:high+1])


def merge_sort(li):
    return _merge_sort(li, 0, len(li)-1)


li = list(range(16))
random.shuffle(li)
print(li)
merge_sort(li)

print(li)

'''
时间复杂度O(nlgn)
'''