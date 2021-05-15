"""
广度优先搜索算法
"""


def search(G, s):
    '''

    :param G:节点弧关联矩阵
    :param s:起始点
    :return:
    '''
    unmarked = [i + 1 for i in range(len(G))]  # unmarked=[1,2,...,n]
    pred = [0] * len(G)
    order = [0] * len(G)
    unmarked[s - 1] = 0
    pred[s - 1] = 0
    next = 1
    order[s - 1] = next
    LIST = []
    LIST.append(s)
    while LIST:
        i = LIST.pop(0)
        for (index, value) in enumerate(G[i - 1]):
            if value == 1:
                for j in range(len(G)):
                    if G[j][index] == -1 and unmarked[j] != 0:
                        unmarked[j] = 0
                        pred[j] = i
                        next += 1
                        order[j] = next
                        LIST.append(j + 1)


    return (pred, order)


G = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
     [-1, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, -1, -1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, -1, 0, -1, 1, -1, 0],
     [0, 0, 0, 0, -1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, -1, 0, -1]]
s = 1
(pred, order) = search(G, s)
print(pred)
print(order)
