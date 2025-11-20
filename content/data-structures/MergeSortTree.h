/**
 * Author:
 * Description:
 * usage: t[n+i] = {x};
 */

const int N = 1<<18;
vi t[2*N];
int n;
void build() {
    for(int i=n-1; i>0; i--)
        merge(all(t[i<<1]), all(t[i<<1|1]), back_inserter(t[i]));
}
void modify(int p, int v) {
    for (t[p+=n]=v; p>1; p>>=1) t[p>>1]=t[p]+t[p^1];
}
int query(int l, int r, int c, int d) {
  int res = 0;
  for(l+=n, r+=n; l<r; l>>=1, r>>=1){
    if(l&1){
        res += (upper_bound(all(t[l]), d) - lower_bound(all(t[l]), c));
        l++;}
    if(r&1){r--;
        res += (upper_bound(all(t[r]), d) - lower_bound(all(t[r]), c));}
  }
  return res;
}
