'''
寻找网络的拓扑序
'''


def topological_ordering(G):
    indegree = [0] * len(G)
    order = [0] * len(G)
    for j in range(len(G)):
        for index in range(len(G[j])):
            if G[j][index] == -1:
                indegree[j] += 1
    LIST = []
    next = 0
    for i in range(len(indegree)):
        if indegree[i] == 0:
            LIST.append(i)
    while LIST:
        i = LIST.pop()
        next += 1
        order[i] = next
        for index in range(len(G[i])):
            if G[i][index] == 1:
                for j in range(len(G)):
                    if G[j][index] == -1:
                        indegree[j] -= 1
                        if indegree[j] == 0:
                            LIST.append(j)
    if next < len(G):
        return 'the network contains a directed cycle'
    else:
        return order


G = [[1, 1, 0, 0, 0, 0, 0, 0, 0, -1],
     [-1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, -1, -1, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, -1, 0, -1, 1, -1, 0, 0],
     [0, 0, 0, 0, -1, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, -1, 0, -1, 0]]
order = topological_ordering(G)
print(order)
