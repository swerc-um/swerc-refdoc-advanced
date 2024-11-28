"""
 * Author: X
 * Description: Finds all biconnected components in an undirected graph.
 * In a biconnected component there are at least two distinct paths between any two nodes.
 * Note that a node can be in several components.
 * An edge which is not in a component is a bridge (not part of any cycle).
 * Time: O(E + V)
 * Status: tested
"""

class BiconnectedComponents:
    def __init__(self, graph):
        self.n = n = len(graph)
        self.m = sum(len(dsts) for dsts in graph) >> 1
        self.nbcs, self.bcvp, self.graph = 0, [], graph
        if n == 0: self.nbcs = 0; return
        used, parent, order = bytearray(n),[0]*n,[0]*n
        def dfs(start, idx):
            Q, parent[start] = [start], -1
            while Q:
                cur = Q.pop()
                if used[cur]: continue
                used[cur], order[idx] = 1, cur
                idx += 1
                for dst in graph[cur]:
                    if not used[dst]:
                        parent[dst] = cur; Q.append(dst)
            return idx
        idx = 0
        for s in range(n):
            if not used[s]: idx = dfs(s, idx)
        v2dfs = [0] * n
        for i in range(n): v2dfs[order[i]] = i
        low = v2dfs[:]
        for p in range(n):
            for e in graph[p]:
                low[p] = min(low[p], v2dfs[e])
        for i in reversed(range(n)):
            p = order[i]
            pp = parent[p]
            if pp >= 0: low[pp] = min(low[pp], low[p])
        nbcs = 0
        for p in order:
            if parent[p] < 0: continue
            pp = parent[p]
            #if low[p] >= v2dfs[pp]:cut_nodes.add(pp)
            #if low[p] > v2dfs[pp]:cut_edges.append((pp, p))
            if low[p] < v2dfs[pp]:
                low[p] = low[pp];self.bcvp.append((low[p], p))
            else:
                low[p] = nbcs; nbcs += 1
                self.bcvp.append((low[p], pp));self.bcvp.append((low[p], p))
        for s in range(n):
            if not graph[s]:
                self.bcvp.append((nbcs, s)); nbcs += 1
        self.nbcs = nbcs
    def __len__(self): return self.nbcs
    def bcc(self):
        bcc_ = [[] for _ in range(self.nbcs)]
        for idx, v in self.bcvp: bcc_[idx].append(v)
        return bcc_
    def merged_bcc(self):
        N, bcc_, repr_ = 0, [], [-1] * self.n
        for vlst in self.bcc():
            if len(vlst) <= 2: continue
            to_merge = []
            for v in vlst:
                if repr_[v] == -1: repr_[v] = N
                else: to_merge.append(repr_[v])
            if to_merge == []:
                bcc_.append(vlst); N += 1
            else:
                main = min(to_merge)
                for v in vlst: repr_[v] = main
                for i in to_merge:
                    for v in bcc_[i]: repr_[v] = main
        BCCs = [[] for _ in range(N)]
        for v in range(self.n):
            if repr_[v] == -1:
                repr_[v] = N; BCCs.append([v]); N += 1
            else: BCCs[repr_[v]].append(v)
        return BCCs, repr_