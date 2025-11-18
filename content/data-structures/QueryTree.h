/**
 * Author: X
 * Description:
 */

struct QueryTree {
    vector<vector<query>> t;
    RollbackUF dsu;
    int T;
    QueryTree(int T, int n) : t(4*T+4), dsu(n), T(T) {}
    void add_to_tree(int v, int l, int r, int ul, int ur, query& q) {
        if (ul > ur) return;
        if (l == ul && r == ur) {
            t[v].push_back(q);
            return;
        }
        int m = (l + r) / 2;
        add_to_tree(2*v, l, m, ul, min(ur, m), q);
        add_to_tree(2*v+1, m+1, r, max(ul, m+1), ur, q);
    }
    void add_query(query q, int l, int r) {
        add_to_tree(1, 0, T-1, l, r, q);
    }
    void dfs(int v, int l, int r, vector<int>& ans) {
        int snapshot = dsu.time();
        for (query& q : t[v]) {
            dsu.join(q.v, q.u);
        }
        if (l == r) ans[l] = dsu.comps;
        else {
            int m = (l+r) / 2;
            dfs(2*v, l, m, ans);
            dfs(2*v+1, m+1, r, ans);
        }
        dsu.rollback(snapshot);
    }
    vector<int> solve() {
        vector<int> ans(T);
        dfs(1, 0, T-1, ans);
        return ans;
    }
};
