/**
 * Author: Simon Lindholm
 * License: CC0
 * Source: Codeforces
 * Description: Given $a[i] = \min_{lo(i) \le k < hi(i)}(f(i, k))$ where the (minimal)
 * optimal $k$ increases with $i$, computes $a[i]$ for $i = L..R-1$.
 * Usage: Cost of dividing an array into k subarrays, cost for a subarray is square of sum of values
 * Time: $O((N + (hi-lo)) \log N)$
 * Status: tested on http://codeforces.com/contest/321/problem/E
 */

int m, n; vlli a;
vector<ll> dp0, dp1;
 
ll C(int i, int j){
    return (a[j+1]-a[i])*(a[j+1]-a[i]);
}
 
struct DP {
    int lo(int ind) { return 0; }
    int hi(int ind) { return ind; }
    ll f(int ind, int k) { return (k ? dp0[k-1] : 0) + C(k, ind); }
    void store(int ind, int k, ll v) { dp1[ind] = v; }
    void rec(int L, int R, int LO, int HI) {
        if (L >= R) return;
        int mid = (L + R) >> 1;
        pair<ll, int> best(LLONG_MAX, LO);
        for (int k = max(LO, lo(mid)); k <= min(HI, hi(mid)); ++k)
            best = min(best, make_pair(f(mid, k), k));
        store(mid, best.second, best.first);
        rec(L, mid, LO, best.second+1);
        rec(mid+1, R, best.second, HI);
    }
    void solve(int L, int R) { rec(L, R, INT_MIN, INT_MAX); }
};
 
ll solve() {
    dp0.assign(n, 0); dp1.assign(n, 0);
    for (int i = 0; i < n; i++)
        dp0[i] = C(0, i);
    struct DP DC;
    for (int i = 1; i < m; i++) {
        DC.solve(0, n);
        dp0 = dp1;
    }
    return dp0[n - 1];
}
a.assign(n+1, 0);
for(int i=0; i<n; i++){
    int x; cin >> x;
    a[i+1] = a[i]+x;
}
cout << solve() << endl;
