/**
 * Author:
 * Description:
 */

const int N = 1<<18;
vi tree[2*N];
int n;
void build() {
    for(int i=n-1; i>0; i--)
        merge(all(tree[i<<1]), all(tree[i<<1|1]), back_inserter(tree[i]));
}
int query(int l, int r, int c, int d) {
  int res = 0;
  for(l+=n, r+=n; l<r; l>>=1, r>>=1){
    if(l&1){
        res += (upper_bound(all(tree[l]), d) - lower_bound(all(tree[l]), c));
        l++;}
    if(r&1){r--;
        res += (upper_bound(all(tree[r]), d) - lower_bound(all(tree[r]), c));}
  }
  return res;
}
