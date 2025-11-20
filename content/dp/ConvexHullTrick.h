/**
 * Author:
 * Description:
 */

double slope(int i, int j) { return (double)(dp[i] - dp[j]) / (a[i].x - a[j].x); }
deque<ll> q;
q.push_back(0);
for (int i = 1; i <= n; i++) {
	while (q.size() > 1 && slope(q[0], q[1]) >= a[i].y) q.pop_front();
	ll j = q.front();
	dp[i] = max(dp[i - 1], a[i].x * a[i].y - a[i].a + dp[j] - a[j].x * a[i].y);
	while (q.size() > 1 && slope(q[q.size() - 2], q.back()) <= slope(q.back(), i))
		q.pop_back();
	q.push_back(i);
}
cout << dp[n];