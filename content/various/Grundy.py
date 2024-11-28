"""
 * Author: X
 * Description: Computes the Minimum EXcluded for a given state. To convert to iterative version
 * Time: $O(N \cdot M)$, \( N \) number of states, \( M \) average number of moves per state.
"""

n = 1000
mex = [None] * (n+1)
mex[0] = 0; mex[1] = 1
def grundyValue(n):
    if mex[n] is not None:
        return mex[n]
    excluded = {grundyValue(n-2)}
    for i in range(2, n):
        excluded.add(grundyValue(i-2) ^ grundyValue(n-i-1))
    res = 0
    while res in excluded:
        res += 1
    mex[n] = res
    return res
