/**
 * Author: X
 * Description: In a DAG, the size of a minimum general path cover equals the size of a maximum antichain.
 * Min Node-disjoint path cover -> N - MCBM (edge u-v si edge de u à v).
 * Min General path cover -> N - MCBM (modifié: edge u-v si chemin de u à v)
 * Usage: Produire un graphe biparti H(V-, V+, E) avec V-, V+ étant des copies de V, et (u-, v+) appartient à E ssi (u, v) appartient à A.
*/

vi ml(n, -1), mr(n, -1);
for (int i=0; i<n; i++) {
    if (~hk.l[i]){
        ml[i] = hk.l[i];
        mr[hk.l[i]] = i;
    }
}
vi part(n);
vvi chains;
for(int v=0; v<n; v++){
    if(ml[v] != -1) continue;
    int u = v;
    vi chain;
    while (u != -1){
        chain.pb(u+1);
        part[u] = 1;
        u = mr[u];
    }
    reverse(chain.begin(), chain.end());
    chains.pb(chain);
}
