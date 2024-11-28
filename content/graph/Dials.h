/**
 * Author: X
 * Description: Dial's algorithm, Faster than dijkstra for graphs with weights <= 10
 * Time: $O(V \cdot lim + E)$.
*/
void dials(int st, vector<vpii> adj, int lim=10){
    int n = sz(adj);
    vector<int> dist(n, -1);
    vector<vector<int>> Qs(lim + 1);
    dist[st] = 0; Qs[0].push_back(st);
    for (int d = 0, mx = 0; d <= mx; d++) {
        for (auto& Q = Qs[d % (lim + 1)]; Q.size();) {
            int cur = Q.back(); Q.pop_back();
            if (dist[cur] != d) continue;
            for (const auto& [nxt, cost] : adj[cur]) {
                if (dist[nxt] == -1 || dist[nxt] > d + cost) {
                    dist[nxt] = d + cost;
                    Qs[dist[nxt] % (lim + 1)].push_back(nxt);
                    mx = max(mx, dist[nxt]);
                }
            }
        }
    }
}