"""
 * Author: X
 * Description: Preprocess the string to insert '\#'
 * between each character to handle even-length palindromes
 * Time: $O(N)$
"""

def longest_pal_substr(s):
    t = '#'.join('^{}$'.format(s))
    n = len(t); p = [0] * n
    center, right = 0, 0
    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        while t[i+p[i]+1] == t[i-p[i]-1]: p[i] += 1
        if i + p[i] > right: center, right = i, i + p[i]
    max_len = max(p)
    center_idx = p.index(max_len)
    start_idx = (center_idx-max_len)>>1
    return s[start_idx:start_idx+max_len]