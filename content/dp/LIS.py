"""
 * Author: X
 * Description: Compute LIS
 * Time: $O(N \log N)$
"""

def longest_increasing_subsequence(lst):
    idxs = []
    nums = []
    for n in lst:
        idx = bisect.bisect_left(nums, n)
        if idx == len(nums):
            nums.append(n)
        else:
            nums[idx] = n
        idxs.append(idx)
    ct = len(nums) - 1
    ret = []
    ret_idx = []
    for i in range(len(lst) - 1, -1, -1):
        if idxs[i] == ct:
            ret.append(lst[i])
            ret_idx.append(i)
            ct -= 1
    ret.reverse()
    ret_idx.reverse()
    return [ret, ret_idx]