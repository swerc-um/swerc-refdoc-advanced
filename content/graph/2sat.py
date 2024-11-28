"""
 * Author: X
 * Description: Solve 2SAT
 * Time: O(N)
"""

class TwoSat:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2*n)]
    def _imply(self, x, y):
        self.graph[x].append(y if y >= 0 else 2*self.n+y)
    def either(self, x, y):
        self._imply(~x, y)
        self._imply(~y, x)
    def set(self, x):
        self._imply(~x, x)
    def implies(self, x, y):
        self.either(~x, y)
    def solve(self):
        SCC = tarjan(self.graph)
        order = [0] * (2 * self.n)
        for i, comp in enumerate(SCC):
            for x in comp: order[x] = i
        for i in range(self.n):
            if order[i] == order[~i]: return False, None
        return True,[+(order[i] > order[~i])for i in range(self.n)]