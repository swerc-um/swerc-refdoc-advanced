"""
 * Author: X
 * Description: size $10^6$ for $10^5$ words, $5*10^5$ seems to work too
 * Time: $O(N)$
"""

trie, j = [-1]*int(27*1e6), 27
#insert list of words
for w in words:
    i = 0
    for char in w:
        c = ord(char) - 97
        if trie[i+c]==-1: trie[i+c]=j; j+=27
        i = trie[i + c]
    trie[i + 26] = 1
#check if w in trie
i = 0
for char in w:
    c = ord(char) - 97
    i = trie[i + c]
    if i == -1:  break
    if trie[i + 26] == 1: pass# this is a valid word