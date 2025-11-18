/**
 * Author: X
 * Description:
*/

vi cover(vector<pii>& ed, int n, int m) {
    vvi g(n);
    for(auto[u, v]: ed) g[u].pb(v);
	vi match(m, -1);
    HopcroftKarp hk(n, m, ed);
    int res = hk.ans;
    for(int i=0; i<n; i++){
        if(~hk.l[i]){
            match[hk.l[i]] = i; // mp(i, hk.l[i]);
        }
    }
	vector<bool> lfound(n, true), seen(m);
	for (int it : match) if (it != -1) lfound[it] = false;
	vi q, cover;
	rep(i,0,n) if (lfound[i]) q.push_back(i);
	while (!q.empty()) {
		int i = q.back(); q.pop_back();
		lfound[i] = 1;
		for (int e : g[i]) if (!seen[e] && match[e] != -1) {
			seen[e] = true;
			q.push_back(match[e]);
		}
	}
	rep(i,0,n) if (!lfound[i]) cover.push_back(i);
	rep(i,0,m) if (seen[i]) cover.push_back(n+i);
	assert(sz(cover) == res);
	return cover;
}
