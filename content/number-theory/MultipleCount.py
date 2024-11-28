"""
 * Author: X
 * Description: Number integers within the interval 1,2,\ldots,n that are divisible by at least one of the prime numbers.
"""

nb = 0
for mask in range(1, 1<<len(primes)):
    num = 1
    for i in range(len(primes)):
        if mask >> i & 1:
            num *= primes[i]
        if num > n:
            break
    if mask.bit_count() % 2:
        nb += n // num
    else:
        nb -= n // num
