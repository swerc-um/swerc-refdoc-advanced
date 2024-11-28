"""
 * Author: X
 * Description: Rolling hashes, use M=1e9+7, P1=31, P2=37
 * Time: $O(N)$
"""

def create_string_hash(string, n, p, mod):
    hash_p, powers = [0] * (n + 1), [1] * (n + 1)
    for i in range(1, n + 1): powers[i] = (powers[i - 1] * p) % mod
    for i in range(n): hash_p[i+1]=(hash_p[i]*p+(ord(string[i])-ord("a")+1))%mod
    return hash_p, powers

def get_hash(hash_p, powers, mod, i, j):
    # Returns the hash of the substring s[i:j] (j excluded) 
    return (hash_p[j] - hash_p[i] * powers[j-i]) % mod
