"""
 * Author: X
 * Description: Couplage parfait de profit maximal
 *  - si minimal, changer signe des poids
 *  - si abs(U) > abs(V), ajouter sommets à V reliés à
 *    tous les sommets de U par un poids 0
 *  - si graph non complet, le compléter avec arêtes
 *    de poids float('-inf')
 * Time: O(\text{abs}(U)^2 \times \text{abs}(V))
 * Status: Tested
"""

def kuhn_munkres(G, TOLERANCE=1e-6):
    assert len(G) <= len(G[0])
    nU, nV = len(G), len(G[0])
    U, V = range(nU), range(nV)
    mu, mv = [None] * nU, [None] * nV
    lu, lv = [max(row) for row in G], [0] * nV
    for root in U:
        au = [False] * nU; au[root] = True
        Av = [None] * nV
        slack = [(lu[root]+lv[v]-G[root][v],root)for v in V]
        while True:
            (delta, u), v = min(
                (slack[v], v)for v in V if Av[v] is None)
            assert au[u]
            if delta > TOLERANCE:
                for u0 in U:
                    if au[u0]: lu[u0] -= delta
                for v0 in V:
                    if Av[v0] is not None: lv[v0] += delta
                    else:
                        (val, arg) = slack[v0]
                        slack[v0] = (val - delta, arg)
            assert abs(lu[u] + lv[v] - G[u][v]) <= TOLERANCE
            Av[v] = u
            if mv[v] is None: break
            u1 = mv[v]
            assert not au[u1]
            au[u1] = True
            for v1 in V:
                if Av[v1] is None:
                    alt = (lu[u1] + lv[v1] - G[u1][v1], u1)
                    if slack[v1] > alt: slack[v1] = alt
        while v is not None:
            u = Av[v]; prec = mu[u]
            mv[v], mu[u] = u, v; v = prec
    return (mu, sum(lu) + sum(lv))