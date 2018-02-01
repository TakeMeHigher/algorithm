import random
from .timewrap import *

def list_to_buckets(li, iteration):
    """
    :param li: 列表
    :param iteration: 装桶是第几次迭代
    :return:
    """
    buckets = [[] for _ in range(10)]
    for num in li:
        digit = (num // (10 ** iteration)) % 10
        buckets[digit].append(num)
    return buckets

def buckets_to_list(buckets):
    return [num for bucket in buckets for num in bucket]
    # li = []
    # for bucket in buckets:
    #     for num in bucket:
    #         li.append(num)

@cal_time
def radix_sort(li):
    maxval = max(li) # 10000
    it = 0
    while 10 ** it <= maxval:
        li = buckets_to_list(list_to_buckets(li, it))
        it += 1
    return li

li = [random.randint(0,1000) for _ in range(100000)]
radix_sort(li)
