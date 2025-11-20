/**
 * Author:
 * Description: Decomposing Kruskal's algorithm to solve problems about min/max edge weights.
 */

UF dsu(n+m);
vi minw(m);
vvi adj(n+m);
vi c_edge(n+m); iota(all(c_edge), 0);
rep(e,0,m){
    deg[u] ^= 1; deg[v] ^= 1;
    minw[e] = w;
    int ru = dsu.find(u);
    int rv = dsu.find(v);
    if(ru != rv){
        dsu.join(ru, rv);
        adj[n+e].pb(c_edge[ru]);
        adj[n+e].pb(c_edge[rv]);
        c_edge[dsu.find(ru)] = n+e;
    } else {
        adj[n+e].pb(c_edge[ru]);
        c_edge[ru] = n+e;
    }
}