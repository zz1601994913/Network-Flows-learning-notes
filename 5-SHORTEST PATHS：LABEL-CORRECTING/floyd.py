'''
floyd算法
'''
M = 99
A = [
    [M, 6, 4, M, M, M],
    [M, M, 2, 2, M, M],
    [M, M, M, 1, 2, M],
    [M, M, M, M, M, 7],
    [M, M, M, 1, M, 3],
    [M, M, M, M, M, M]
]


def floyd(A):
    d = A
    pred = [[i + 1] * len(A) for i in range(len(A))]
    for i in range(len(A)):
        d[i][i] = 0
    for k in range(len(A)):
        for i in range(len(A)):
            for j in range(len(A)):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    pred[i][j] = pred[k][j]
    return d, pred


[d, pred] = floyd(A)
print(d)
print(pred)
