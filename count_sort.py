# 0 0 1 1 2 4 3 3 1 4 5 5
import random
import copy
from .timewrap import *

@cal_time
def count_sort(li, max_num = 100):
    count = [0 for i in range(max_num+1)]
    for num in li:
        count[num]+=1
    li.clear()
    for i, val in enumerate(count):
        for _ in range(val):
            li.append(i)

@cal_time
def sys_sort(li):
    li.sort()

li = [random.randint(0,100) for i in range(100000)]
li1 = copy.deepcopy(li)
count_sort(li)
sys_sort(li1)

