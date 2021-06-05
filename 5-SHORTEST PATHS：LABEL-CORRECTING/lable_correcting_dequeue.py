M = 99
A = [
    [M, 2, 2, M, M],
    [M, M, M, 4, 3],
    [M, M, M, M, 1],
    [M, M, M, M, 3],
    [M, M, M, M, M]
]
s = 1


def lable_correcting_fifo(A, s):
    d = [99] * len(A)
    pred = [0] * len(A)
    d[s - 1] = 0
    LIST = [s]  # list中存标号
    while LIST:
        i = LIST.pop(0)
        for j in range(len(A)):
            if d[j] > d[i - 1] + A[i - 1][j]:
                d[j] = d[i - 1] + A[i - 1][j]
                pred[j] = i
                if LIST.count(j + 1) > 0:
                    LIST.insert(0, j + 1)
                else:
                    LIST.append(j + 1)
    return d, pred


[d, pred] = lable_correcting_fifo(A, s)
print(d)
print(pred)
