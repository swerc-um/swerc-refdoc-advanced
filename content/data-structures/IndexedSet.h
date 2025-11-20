/**
 * Author:
 * Description:
 * Usage: indexed_set<pii> s;
 *  s.insert({x[i], i});
 *  s.erase({x[i-k], i-k});
 *  s.find_by_order((k-1)/2)->first;
 *  s.order_of_key(7) //pos el would have
 * Time: $O(\log N)$
 */

#include <bits/extc++.h>
using namespace __gnu_pbds;
template <typename T>
using indexed_set =
    tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;