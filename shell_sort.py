
def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        for i in range(d, len(li)):
            tmp = li[i]
            j = i - d
            while li[j] > tmp and j >= 0:
                li[j+d] = li[j]
                j -= d
            li[j+d] = tmp
        d = d >> 1