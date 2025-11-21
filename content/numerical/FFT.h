/**
 * Author: Ludo Pulles, chilli, Simon Lindholm
 * Date: 2019-01-09
 * License: CC0
 * Description: \texttt{conv(a, b) = c}, where $c[x] = \sum a[i]b[x-i]$.\\
 At most $k$ mismatches :
   Let's fix some character $c$.
We define a polynomial
\[
R_c(x) = \sum_i [\,T[i] = c\,]\, x^i,
\]
that is, we consider only the positions that are equal to $c$ in the text.
We do the same for the pattern, but reversed:
\[
S_c(x) = \sum_i [\,P[i] = c\,]\, x^{\,|P|-1-i}.
\]
The coefficient of $x^{|P|-1}$ of $R * S$
is equal to the number of characters $c$ that match if we try to match $P$
at position $0$ in $T$; the coefficient of $x^{|P|}$ of $R * S$
is equal to the number of characters $c$ that match if we try to match $P$
at position $1$ in $T$, and so on.

 * Time: O(N \log N) with $N = |A|+|B|$ ($\tilde 1s$ for $N=2^{22}$)
 * Status: somewhat tested
 */

using C=complex<double>; const ll mod=998244353;
void fft(vector<C>&a){
	int n=sz(a),L=31-__builtin_clz(n);
	static vector<complex<long double>>R(2,1);
	static vector<C> rt(2,1);
	for(static int k=2;k<n;k*=2){
		R.resize(n);rt.resize(n);
		auto x=polar(1.0L,acos(-1.0L)/k);
		for(int i=k;i<2*k;i++)
			rt[i]=R[i]=i&1?R[i/2]*x:R[i/2];
	}
	vector<int> rev(n);
	for(int i=0;i<n;i++)
		rev[i]=(rev[i/2]|(i&1)<<L)/2;
	for(int i=0;i<n;i++)
		if(i<rev[i])
			swap(a[i],a[rev[i]]);
	for(int k=1;k<n;k*=2){
		for(int i=0;i<n;i+=2*k)
			for(int j=0;j<k;j++){
				auto x=(double*)&rt[j+k],y=(double*)&a[i+j+k];
				C z(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]);
				a[i+j+k]=a[i+j]-z;
				a[i+j]+=z;}}}
template<ll M>
vector<ll> convMod(const vector<ll>&a, const vector<ll>&b){
	if(a.empty() || b.empty()) return {};
	vector<ll> res(sz(a)+sz(b)+1);
	int B=32-__builtin_clz(sz(res)),n=1<<B,cut=int(sqrt(M));
	vector<C> L(n),R(n),outs(n),outl(n);
	for(int i=0;i<sz(a);i++)
		L[i]=C((int)a[i]/cut,(int)a[i]%cut);
	for(int i=0;i<sz(b);i++)
		R[i]=C((int)b[i]/cut,(int)b[i]%cut);
	fft(L),fft(R);
	for(int i=0;i<n;i++){
		int j=-i&(n-1);
		outl[j]=(L[i]+conj(L[j]))*R[i]/(2.0*n);
		outs[j]=(L[i]-conj(L[j]))*R[i]/(2.0*n)/1i;}
	fft(outl),fft(outs);
	for(int i=0;i<sz(res);i++){
		ll av=ll(real(outl[i])+.5),cv=ll(imag(outs[i])+.5);
		ll bv=ll(imag(outl[i])+.5)+ll(real(outs[i])+.5);
		res[i]=((av%M*cut+bv)%M*cut+cv)%M;}
	return res;}
vlli shift(vector<ll> &a, ll v){
	ll n=sz(a)-1;
	vlli f(n+1), g(n+1), i_fact(n+1);
	f[0]=a[0];
	g[n]=1;
	i_fact[0]=1;
	ll fact=1,potk=1;
	for(int i=1;i<n+1;i++){
		fact=fact*i%mod;
		f[i]=fact*a[i]%mod;
		potk=(potk*v%mod+mod)%mod;
		g[n-i]=((potk*inv(fact))%mod+mod)%mod;
		i_fact[i]=inv(fact);}
	auto p = convMod<mod>(f,g);
	vlli res(n+1);
	for(int i=0;i<n+1;i++)
		res[i]=(p[i+n]*i_fact[i]%mod+mod)%mod;
	return res;}
