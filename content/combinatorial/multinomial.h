/**
 * Author: Mattias de Zalenski, Fredrik Niemelä, Per Austrin, Simon Lindholm
 * Date: 2002-09-26
 * Source: Max Bennedich
 * Description: Count the number of ways to divide $k_1 + k_2 + \cdots + k_n$ objects into $n$ groups of sizes $k_1, k_2, \ldots, k_n$.\\
 * Computes $\displaystyle \binom{k_1 + \dots + k_n}{k_1, k_2, \dots, k_n} = \frac{(\sum k_i)!}{k_1!k_2!...k_n!}$.
 * Status: Tested on kattis:lexicography
 */

ll multinomial(vi& v) {
	ll c = 1, m = v.empty() ? 1 : v[0];
	rep(i,1,sz(v)) rep(j,0,v[i]) c = c * ++m / (j+1);
	return c;
}