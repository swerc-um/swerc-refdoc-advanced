"""
 * Author: X
 * Description: Circulation with lowerbounds d(e) <= f(e) <= c(e)
 * Time: X
"""

graph = [{} for _ in range(N+2)]
isum, osum, edges = [0]*N, [0]*N, []
for _ in range(M):
    a, b, d, c = map(int,input().split())
    add_edge(graph, a, b, c-d)
    isum[b]+=d; osum[a]+=d
s, t = N, N+1
indemands = outdemands = 0
for v in range(N):
    need = isum[v] - osum[v]
    if need < 0:
        add_edge(graph, v, t, -need); outdemands -= need
    if need > 0:
        add_edge(graph, s, v, need); indemands += need
if indemands != outdemands: print("NON")
else:
    _, mf = dinic(s, t, graph)
    print("OUI" if mf == indemands else "NON")