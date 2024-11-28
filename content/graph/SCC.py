"""
 * Author: X
 * Description: SCC
 * Time: O(N)
"""


def tarjan(G):
    n = len(G)
    SCC, S, P = [], [], []
    Q, st = list(range(n)), [0] * n
    while Q:
        node = Q.pop()
        if node < 0:
            d = st[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:]; P.pop()
                for v in SCC[-1]:
                    st[v] = -1
        elif st[node] > 0:
            while P[-1] > st[node]:P.pop()
        elif st[node] == 0:
            S.append(node)
            P.append(len(S))
            st[node] = len(S)
            Q.append(~node)
            Q.extend(G[node])
    return SCC