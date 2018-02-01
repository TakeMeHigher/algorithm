from .timewrap import *
import random

def _sift(li, low, high):
    """
    :param li:
    :param low: 堆根节点的位置
    :param high: 堆最有一个节点的位置
    :return:
    """
    i = low  # 父亲的位置
    j = 2 * i + 1  # 孩子的位置
    tmp = li[low]  # 原省长
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子存在并且右孩子更大
            j += 1
        if tmp < li[j]:  # 如果原省长比孩子小
            li[i] = li[j]  # 把孩子向上移动一层
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp  # 省长放到对应的位置上(干部)
            break
    else:
        li[i] = tmp  # 省长放到对应的位置上(村民/叶子节点)


def sift(li, low, high):
    """
    :param li:
    :param low: 堆根节点的位置
    :param high: 堆最有一个节点的位置
    :return:
    """
    i = low         # 父亲的位置
    j = 2 * i + 1   # 孩子的位置
    tmp = li[low]   # 原省长
    while j <= high:
        if j + 1 <= high and li[j+1] > li[j]: # 如果右孩子存在并且右孩子更大
            j += 1
        if tmp < li[j]: # 如果原省长比孩子小
            li[i] = li[j]  # 把孩子向上移动一层
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


@cal_time
def heap_sort(li):
    n = len(li)
    # 1. 建堆
    for i in range(n//2-1, -1, -1):
        sift(li, i, n-1)
    # 2. 挨个出数
    for j in range(n-1, -1, -1):    # j表示堆最后一个元素的位置
        li[0], li[j] = li[j], li[0]
        # 堆的大小少了一个元素 （j-1）
        sift(li, 0, j-1)


li = list(range(10000))
random.shuffle(li)
heap_sort(li)
print(li)

# li=[2,9,7,8,5,0,1,6,4,3]
# sift(li, 0, len(li)-1)
# print(li)

''''
建立堆
得到堆顶元素，为最大元素
去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
堆顶元素为第二大元素。
重复步骤3，直到堆变空。

时间复杂度O(nlgn)
'''