/**
 * Author: X
 * Date: X
 * Source: X
 * Description: Simple undirected unweighted graph
 * A graph is **chordal** if it does not have an induced cycle of length four or more.
 * A **perfect elimination ordering** is an ordering of the vertices such that for every
 * vertex v, v and the neighbors of v that appear after it in the ordering form a clique.
 * It can be shown that a graph is chordal if and only if it has a perfect elimination ordering.
 * If the graph is chordal, find a perfect elimination ordering.
 * If the graph is not chordal, find an induced cycle of length four or more.
 * - Constraints :
 * \[1 \leq N \leq 2 \times 10^5\]
 * \[0 \leq M \leq 2 \times 10^5\]
 * To color the graph greedily according to the PEO:
 * Starting from the last vertex in the PEO, assign colors to each vertex in order,
 * choosing the smallest available color that hasn't been assigned to its already-colored neighbors.
 * Because the graph is chordal, each vertex's neighbors form a clique among
 * vertices appearing later in the PEO.
 * Time: X
 * Status: Tested
 */

struct Set {
    list<int> L; int last;
    Set() { last = 0; }
};
struct PEO {
    int N;
    vector<vector<int> > g;
    vector<int> vis, res;
    list<Set> L;
    vector<list<Set>::iterator> ptr;
    vector<list<int>::iterator> ptr2;
    PEO(int n, vector<vector<int> > _g) {
        N = n; g = _g;
        for (int i = 1; i <= N; i++) sort(g[i].begin(), g[i].end());
        vis.resize(N + 1); ptr.resize(N + 1); ptr2.resize(N + 1);
        L.push_back(Set());
        for (int i = 1; i <= N; i++) {
            L.back().L.push_back(i);
            ptr[i] = L.begin(); ptr2[i] = prev(L.back().L.end());
        }
    }
    pair<bool, vector<int>> Run() {
        // lexicographic BFS
        int time = 0;
        while (!L.empty()) {
            if (L.front().L.empty()) { L.pop_front(); continue; }
            auto it = L.begin();
            int n = it->L.front(); it->L.pop_front();
            vis[n] = ++time;
            res.push_back(n);
            for (int next : g[n]) {
                if (vis[next]) continue;
                if (ptr[next]->last != time) {
                    L.insert(ptr[next], Set()); ptr[next]->last = time;
                }
                ptr[next]->L.erase(ptr2[next]); ptr[next]--;
                ptr[next]->L.push_back(next);
                ptr2[next] = prev(ptr[next]->L.end());
            }
        }
        // PEO existence check
        for (int n = 1; n <= N; n++) {
            int mx = 0;
            for (int next : g[n]) if (vis[n] > vis[next]) mx = max(mx, vis[next]);
            if (mx == 0) continue;
            int w = res[mx - 1];
            for (int next : g[n]) {
                if (vis[w] > vis[next] && !binary_search(g[w].begin(), g[w].end(), next)){
                    vector<int> chk(N+1), par(N+1, -1); // If w and next are not connected, the graph is not chordal
                    deque<int> dq{next}; chk[next] = 1;
                    while (!dq.empty()) {
                        int x = dq.front(); dq.pop_front();
                        for (auto y : g[x]) {
                            if (chk[y] || y == n || y != w && binary_search(g[n].begin(), g[n].end(), y)) continue;
                            dq.push_back(y); chk[y] = 1; par[y] = x;
                        }
                    }
                    vector<int> cycle{next, n};
                    for (int x=w; x!=next; x=par[x]) cycle.push_back(x);
                    return {false, cycle};
                }
            }
        }
        reverse(res.begin(), res.end());
        return {true, res};
    }
};
vector<vector<int>> G(N+1);
for(int i=1,s,e; i<=M; i++)
    cin >> s >> e, G[s+1].push_back(e+1), G[e+1].push_back(s+1);
auto [flag,vec] = PEO(N, G).Run();
if(flag){
    cout << "YES\n";
    for(auto i : vec) cout << i - 1 << " ";
}
else{
    cout << "NO\n" << vec.size() << "\n";
    for(auto i : vec) cout << i - 1 << " ";
}
