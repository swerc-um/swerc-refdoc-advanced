/**
 * Author:
 * Description:
 */

void merge(set<int>& s, set<int>& t) {
	if (s.size() < t.size()) s.swap(t);
	for (auto x : t) s.insert(x);
	t = {};
}
function<void(int,int)> dfs = [&](int v, int par) {
    for(int u : adj[v]){
        if(u == par) continue;
        dfs(u, v);
        merge(vset[v], vset[u]);
    }
    vset[v].insert(p[v]);
    for(auto T : query[v]){
        auto [i, l, r] = T;
        auto it = vset[v].lower_bound(l);
        ans[i] = it != vset[v].end() && *it <= r;
    }
};
dfs(1, 0);