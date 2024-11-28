"""
 * Author: X
 * Description: Prime factors of N
 * Time: $O(\sqrt N)$.
"""

def getPrimeFactors(n):
    res = {}
    if n % 2 == 0:
        res[2] = 0
        while n % 2 == 0:
            res[2] += 1
            n //= 2
    for i in range(3,int(n**.5)+1,2):
        if n % i == 0:
            res[i] = 0
            while n % i == 0:
                res[i] += 1
                n //= i
    if n > 1: res[n] = 1
    return res

def getDivisors(n):
    primeFactors = getPrimeFactors(n)
    res, pw = [], 1
    for factor in primeFactors:
        pw *= primeFactors[factor] + 1
    for i in range(pw):
        divisor = 1
        for factor in primeFactors:
            divisor *= factor ** (i % (primeFactors[factor] + 1))
            i //= primeFactors[factor] + 1
        res.append(divisor)
    return res
