/**
 * Author: Stjepan Glavina, chilli
 * Date: 2019-05-05
 * License: Unlicense
 * Source: https://github.com/stjepang/snippets/blob/master/convex_hull.cpp
 * Description:
\\\begin{minipage}{75mm}
Returns a vector of the points of the convex hull in counter-clockwise order.
Points on the edge of the hull between two other points are not considered part of the hull.
\end{minipage}
\begin{minipage}{15mm}
\vspace{-6mm}
\includegraphics[width=\textwidth]{content/geometry/ConvexHull}
\vspace{-6mm}
\end{minipage}
 * Time: O(n \log n)
 * Status: stress-tested, tested with kattis:convexhull
*/

#include "Point.h"

typedef Point<ll> P;
vector<P> convexHull(vector <P> pt) {
    int n = sz(pt);
    sort(all(pt), [&](P a, P b) {
        return a.x == b.x ? a.y < b.y : a.x < b.x;
    });
    vector<P> ans = {pt[0]};
    for (int t : {0, 1}) {
        int m = sz(ans);
        for (int i = 1; i < n; ++i) {
            while (sz(ans) > m && ans[sz(ans)-2].cross(ans.back(), pt[i]) < 0)
                ans.pop_back();
            ans.pb(pt[i]);}
        reverse(all(pt));}
    ans.pop_back();
    return ans;
}