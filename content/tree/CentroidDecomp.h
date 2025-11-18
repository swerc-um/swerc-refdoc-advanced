/**
 * Author: X
 * Description: Centroid Decomposition is a divide and conquer technique for trees.
 * Works by repeated splitting the tree and each of the resulting subgraphs at the centroid,
 * producing $\mathcal{O}(\log N)$ layers of subgraphs.
 * Time: $O(\log N)$
 */

vvi adj; vi subtree_size;
vi min_dist; vector<bool> is_removed;
vvpii ancestors;
int get_subtree_size(int node, int parent = -1) {
	subtree_size[node] = 1;
	for (int child : adj[node]) {
		if (child == parent || is_removed[child]) { continue; }
		subtree_size[node] += get_subtree_size(child, node);}
	return subtree_size[node];
}
int get_centroid(int node, int tree_size, int parent = -1) {
	for (int child : adj[node]) {
		if (child == parent || is_removed[child]) { continue; }
		if (subtree_size[child] * 2 > tree_size) {
			return get_centroid(child, tree_size, node);}}
	return node;
}
void get_dists(int node, int centroid, int parent = -1, int cur_dist = 1) {
	for (int child : adj[node]) {
		if (child == parent || is_removed[child]) { continue; }
		cur_dist++;
		get_dists(child, centroid, node, cur_dist);
		cur_dist--;
	}
	ancestors[node].push_back({centroid, cur_dist});}
void build_centroid_decomp(int node = 0) {
	int centroid = get_centroid(node, get_subtree_size(node));
	for (int child : adj[centroid]) {
		if (is_removed[child]) { continue; }
		get_dists(child, centroid, centroid);}
	is_removed[centroid] = true;
	for (int child : adj[centroid]) {
		if (is_removed[child]) { continue; }
		build_centroid_decomp(child);}
}
void paint(int node) {
	for (auto &[ancestor, dist] : ancestors[node]) {
		min_dist[ancestor] = min(min_dist[ancestor], dist);}
	min_dist[node] = 0;}
void query(int node) {
	int ans = min_dist[node];
	for (auto &[ancestor, dist] : ancestors[node]) {
		if (!dist) continue;
		ans = min(ans, dist + min_dist[ancestor]);}
	cout << ans << "\n";}
