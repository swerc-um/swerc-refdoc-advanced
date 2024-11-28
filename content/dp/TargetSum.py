"""
 * Author: X
 * Description: Equivalent to
 * bitset<1000001> dp; dp.set(0);
 * for(int j = 0; j < n; j++) dp |= dp << s[j];
 * Time: $O(N \cdot MAX)$
"""

MAX = 1000001
dp = [0] * MAX
dp[0] = 1
for x in a:
    for j in range(MAX-1, x-1, -1):
        dp[j] |= dp[j-x]
