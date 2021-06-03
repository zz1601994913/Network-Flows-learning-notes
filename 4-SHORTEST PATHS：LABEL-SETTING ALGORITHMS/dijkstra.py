'''
dijkstra算法
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


def dijkstra(A, s):
    S = []
    S_temp = [i for i in range(1, len(A) + 1)]
    M = 999
    d = [M] * len(A)
    pred = [0] * len(A)
    d[s - 1] = 0
    pred[s - 1] = 0
    while len(S) < len(A):
        temp = 99
        i = 0
        for j in range(len(S_temp)):
            if temp > d[S_temp[j] - 1]:
                temp = d[S_temp[j] - 1]
                i = S_temp[j] - 1  # i是索引
        S.append(i + 1)
        S_temp.remove(i + 1)
        for j in range(len(A)):
            if d[j] > d[i] + A[i][j]:
                d[j] = d[i] + A[i][j]
                pred[j] = i + 1
    return d, pred


[d, pred] = dijkstra(A, s)
print(d)
print(pred)
