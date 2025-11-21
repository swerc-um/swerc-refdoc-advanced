/**
 * Author:
 * Description: Binary Grouping for Multiple Knapsack
 * Time: $O(W\sum\limits_{i=1}^{n}\log k_i)$
 */

index = 0;
for (int i = 1; i <= n; i++) {
  int c = 1, p, h, k;
  while (k > c) {
    k -= c;
    list[++index].w = c * p;
    list[index].v = c * h;
    c *= 2;
  }
  list[++index].w = p * k;
  list[index].v = h * k;
}

for (each item) {
  if (0-1 knapsack)
    Apply 0-1 knapsack code;
  else if (complete knapsack)
    Apply complete knapsack code;
  else if (multiple knapsack)
    Apply multiple knapsack code;
}