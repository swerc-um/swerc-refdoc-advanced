/**
 * Author:
 * Description: convert the multiple knapsack problem into a maximum queue problem.
 * Time: $O(nW)$.
 */

vi dp(W+1);
for(int i=0; i<n; i++){
    int w, v, k;
    if (w > W) continue;
    vi dq(W+1);
    for(int y=0; y<w; y++){
        deque<int> Q;
        for(int x=0; x<=(W-y)/w; x++){
            int pos = x * w + y;
            int G = dp[pos] - x * v;
            while(!Q.empty() && Q.front() < x-k) Q.pop_front();
            while(!Q.empty() && (dp[Q.back()*w+y] - Q.back()*v <= G)) Q.pop_back();
            Q.push_back(x);
            dq[pos] = dp[Q.front() * w + y] + (x - Q.front()) * v;
        }
    }
    dp = dq;
}