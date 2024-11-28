/** 
 * Author: X
 * Description: RabinKarp rolling hashes in 2d
 * Usage: RK2d\(pattern, masterpiece, 31\)
 * Time: $O(N \cdot M)$
*/

int RK2d(vector<string>&p, vector<string>&m, ll A) {
    int hp=sz(p),wp=sz(p[0]),hm=sz(m),wm=sz(m[0]);
    ll iA=Mod(A).invert(A).x;
    Mod rh=0;
    for(int i=0;i<hp;i++)
        for(int j=0;j<wp;j++)
            rh=rh+Mod(p[i][j])*(Mod(A)^(wp*i+j));
    vector<vector<Mod>>h1d(hm,vector<Mod>());
    for(int i=0;i<hm;i++) {
        Mod ch=0;
        for(int j=0;j<wp;j++)ch=ch+Mod(m[i][j])*(Mod(A)^j);
        h1d[i].push_back(ch);
        for(int j=wp;j<wm;j++) {
            ch=(ch-Mod(m[i][j-wp]))*Mod(iA)+\
            Mod(m[i][j])*(Mod(A)^(wp-1));
            h1d[i].push_back(ch);}}
    vector<vector<Mod>>h2d(hm-hp+1,vector<Mod>(wm-wp+1,Mod(0)));
    for(int j=wp;j<=wm;j++) {
        Mod ch=0;
        for(int i=0;i<hp;i++)ch=ch+h1d[i][j-wp]*(Mod(A)^(i*wp));
        h2d[0][j-wp]=ch;}
    for(int i=hp;i<hm;i++)for(int j=wp;j<=wm;j++)
        h2d[i-hp+1][j-wp]=(h2d[i-hp][j-wp]-h1d[i-hp][j-wp])*\
        (Mod(iA)^wp)+h1d[i][j-wp]*(Mod(A)^(wp*(hp-1)));
    int mt=0;
    for(int i=0;i<=hm-hp;i++)
        for(int j=0;j<=wm-wp;j++)if(h2d[i][j]==rh)mt++;
    return mt;
}