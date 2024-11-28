"""
 * Author: X
 * Description: Union Find
 * Time: $O(\alpha(N))$
"""

class DSU:
    def __init__(self, n):
        self.up = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.up[x] != x:
            self.up[x] = self.find(self.up[x])
        return self.up[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.up[y] = x
        self.size[x] += self.size[y]
        return True
