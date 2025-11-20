#include <bits/stdc++.h>
#include <bits/extc++.h>
#pragma GCC target("avx2")
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
using namespace std;
using namespace __gnu_pbds;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define endl '\n'
typedef long long ll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    sort(all(a)), a.resize(unique(all(a)) - a.begin());
    ll k = rng(); // random 64 bits integer
    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<mt19937::result_type> dist6(1,6); // distribution in range [1, 6]
    cout << fixed << setprecision(6) << dist6(rng) << endl;
}
