"""
 * Author: X
 * Description: Smallest perm
 * Time: O(N \log N)
"""

revgraph = [[] for _ in range(n)]
outdeg = [0] * n
for _ in range(m):
    a, b = map(int,input().split())
    revgraph[b].append(a)
    outdeg[a] += 1
Q = [-node for node in range(n) if outdeg[node] == 0]
heapify(Q)
order = []
while Q:
    node = -heappop(Q)
    order.append(node + 1)
    for neigh in revgraph[node]:
        outdeg[neigh] -= 1
        if outdeg[neigh] == 0:
            heappush(Q, -neigh)
print(*order[::-1])