"""
 * Author: X
 * Description: Dilworth’s theorem states that in a directed acyclic graph, the size of a minimum general path cover equals the size of a maximum antichain.
 * Largeur d'un ordre partiel = taille de la plus grande anti-chaîne.
 * Usage: Produire un graphe biparti H(V-, V+, E) avec V-, V+ étant des copies de V, et (u-, v+) appartient à E ssi (u, v) appartient à A. Retourne partition en chaînes
 * Time: X
"""

def dilworth(graph):
    n = len(graph)
    match = [None] * n
    for a, b in bm.solve():
        match[b] = a
    part = [None] * n
    nb_chains = 0
    for v in range(n - 1, -1, -1):
        if part[v] is None:
            u = v
            while u is not None:
                part[u] = nb_chains
                u = match[u]
            nb_chains += 1
    return part