/**
 * Author:
 * Description:
 */

vpii qq(q);
vi ql(q, 0), qr(q, m);
for(int i=0; i<q; i++){
    int u, v; cin >> u >> v;
    qq[i] = {--u, --v};
}
while(1){
    vvi queries(m+1);
    bool added = false;
    for(int i=0; i<q; i++){
        if(ql[i] < qr[i]){
            queries[(ql[i]+qr[i])>>1].pb(i);
            added = true;
        }
    }
    if(!added) break;
    UF dsu(n);
    for(int i=0; i<m; i++){
        for(int qi: queries[i]){
            auto[x, y] = qq[qi];
            if(dsu.find(x) == dsu.find(y)) qr[qi] = i;
            else ql[qi] = i+1;
        }
        dsu.join(edges[i].first, edges[i].second);
    }
}