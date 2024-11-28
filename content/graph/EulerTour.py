"""
 * Author: X
 * Date: X
 * License: X
 * Source: X
 * Description: Check connectivity
 * - Undirected graph : connected and all nodes have even deg,
 * or only 2 have odd degree
 * - Directed graph : At most one node has out\_i - in\_i = 1
 * and at most one node has in\_i - out\_i = 1
 * - Multigraph : Mind case with only one node
 * Time: $O(N)$
 * Status: Tested
"""

def eulerian_tour(m, s, graph):
    # also works with a multigraph if directed
    P, Q = [], [s]
    while Q:
        u = Q[-1]
        if len(graph[u]):
            v = graph[u].pop()
            # graph[v].discard(u) # if undir
            Q.append(v)
        else:
            P.append(Q.pop())
    return P[::-1] if len(P)==m+1 else -1

def eulerian_tour_undir_multigraph(m, s, graph, rem):
    """
    rem = [[] for _ in range(N)]
    graph[a].append((b, len(graph[b]))); rem[a].append(False)
    graph[b].append((a, len(graph[a])-1)); rem[b].append(False)
    """
    P, Q = [], [s]
    while Q:
        u = Q[-1]
        while len(graph[u]):
            if rem[u][len(graph[u])-1]:
                graph[u].pop()
            else: break
        if len(graph[u]):
            rem[u][len(graph[u])-1] = True
            v, j = graph[u].pop()
            rem[v][j] = True
            Q.append(v)
        else:
            P.append(Q.pop())
    return P[::-1] if len(P)==m+1 else -1