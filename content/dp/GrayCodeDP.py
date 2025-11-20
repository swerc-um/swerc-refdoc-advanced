"""
 * Author:
 * Description: Gray code in $O(2^n)$ instead of $O(n * 2^n)$.
 * Usage: g = m^(m>>1)
 *  rev_g(int g) { int n = 0; for (; g; g >>= 1) n ^= g; }
"""
