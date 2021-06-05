'''
dijkstra算法dial实现
'''
M = 99
A = [
    [M, 6, 4, M, M, M],
    [M, M, M, 2, M, M],
    [M, 2, M, 1, 2, M],
    [M, M, M, M, M, 7],
    [M, M, M, 1, M, 3],
    [M, M, M, M, M, M]
]
s = 1


def dijkstra_dial(A, s):
    C = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if C < A[i][j] < 50:
                C = A[i][j]  # 寻找最大弧长
    buckets = [[] for i in range(C + 1)]
    d = [99] * len(A)
    pred = [0] * len(A)
    d[s - 1] = 0
    buckets[d[s - 1]].append(s)  # 桶里的是标号
    n = 0
    m = 0  # 记录当前桶对应的标签大小
    while n < C + 1:  # n用于记录检测了多少个桶,n=C+1时表示检测了一圈全是空桶
        if buckets[m % (C + 1)]:
            n = 0
            i = buckets[m % (C + 1)].pop(0)
            for j in range(len(A)):
                if d[j] > d[i - 1] + A[i - 1][j]:
                    if d[j] < 99:
                        buckets[d[j] % (C + 1)].remove(j + 1)  # 从原来的桶中移除
                    d[j] = d[i - 1] + A[i - 1][j]
                    pred[j] = i
                    buckets[d[j] % (C + 1)].append(j + 1)
        else:
            m += 1
            n += 1
    return d,pred
[d,pred]=dijkstra_dial(A,s)
print(d,pred)
