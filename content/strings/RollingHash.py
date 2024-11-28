"""
 * Author: X
 * Description: Rolling hashes, use M=1e9+7, P1=31, P2=37
 * Time: $O(N)$
"""

def create_string_hash(string, n, p, mod):
    hash_prefixes = [0] * (n + 1)
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = (powers[i - 1] * p) % mod
    for i in range(n):
        hash_prefixes[i + 1] = (hash_prefixes[i] * p + (ord(string[i]) - ord("a") + 1)) % mod
    return hash_prefixes, powers

def get_hash(hash_prefixes, powers, mod, i, j):
    # Returns the hash of the substring s[i:j] (j excluded) 
    return (hash_prefixes[j] - hash_prefixes[i] * powers[j-i]) % mod
