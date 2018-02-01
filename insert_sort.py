import random
from .timewrap import *

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        # i 表示无序区第一个数
        tmp = li[i] # 摸到的牌
        j = i - 1 # j 指向有序区最后位置
        while li[j] > tmp and j >= 0:
            #循环终止条件： 1. li[j] <= tmp; 2. j == -1
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


li = list(range(10000))
random.shuffle(li)
print(li)
insert_sort(li)
print(li)

'''
列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
O(n2)

'''