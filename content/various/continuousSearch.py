"""
 * Author:
 * Description:
"""
def continuousTernSearch(a, b, f):
    while b-a > 1e-9:
        mid1 = (2*a+b)/3
        mid2 = (a+2*b)/3
        if f(mid1) < f(mid2): b = mid2
        else: a = mid1
    return a
def continuousBinSearch(a, b, f):
    for _ in range(64):
        mid = (a+b)/2
        if f(mid): b = mid
        else: a = mid
    return a
