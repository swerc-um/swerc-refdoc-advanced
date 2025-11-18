/**
 * Author: X
 * Description: Returns block-cut tree
 */

vvi biconnected_components(int n, int m, vvpii &g, vi &is_cutpoint, vi &is_bridge, vi &id) {
	vvi comps;
	vi stk, num(n), low(n);
	is_cutpoint.resize(n);
    is_bridge.resize(m);
	function<void(int, int, int &)> dfs = [&](int node, int par, int &time) {
		num[node] = low[node] = ++time;
		stk.pb(node);
		for (auto [son, i] : g[node]) {
			if (son == par) continue;
			if (num[son]) {
				low[node] = min(low[node], num[son]);
			} else {
				dfs(son, node, time);
				low[node] = min(low[node], low[son]);
				if (low[son] >= num[node]) {
					is_cutpoint[node] = (num[node] > 1 || num[son] > 2);
					comps.pb({node});
					while (comps.back().back() != son) {
						comps.back().pb(stk.back());
						stk.pop_back();
					}
				}
                is_bridge[i] = (low[son] > num[node]);
			}
		}
	};
	int time = 0;
    dfs(0, -1, time);
	id.resize(n);
	function<vvi()> build_tree = [&]() {
		vvi t(1);
		int node_id = 0;
		for (int node = 0; node < n; node++) {
			if (!is_cutpoint[node]) continue;
            id[node] = node_id++;
            t.pb({});
		}
		for (auto &comp : comps) {
			int node = node_id++;
			t.pb({});
			for (int u : comp)
				if (!is_cutpoint[u]) {
					id[u] = node;
				} else {
					t[node].pb(id[u]);
					t[id[u]].pb(node);
				}
		}
		return t;
	};
	return build_tree();
}