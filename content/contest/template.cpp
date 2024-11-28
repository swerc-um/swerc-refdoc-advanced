#include <bits/stdc++.h>
#include <bits/extc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    vi cord;
    cord.erase(unique(cord.begin(),cord.end()),cord.end());  // supprime doublons
    ll k = rng(); // random 64 bits integer
    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<mt19937::result_type> dist6(1,6); // distribution in range [1, 6]
    cout << fixed << setprecision(6) << dist6(rng) << endl;
}