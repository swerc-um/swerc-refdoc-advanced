"""
 * Author: X
 * Description:
 * Linearbase : prend une liste de nombres a et renvoie une base linéaire
 * (ensemble minimal d'el indépendants en termes de bits).
 * Crée une représentation réduite où chaque nombre est une combinaison linéaire unique des nombres dans cette base.
 * Baseinsert : Prend une base b et un nombre x, et essaie insertion (sans redondance = inséré = renvoie True).
 * Time: X
"""

mx_bit=20
def linearbase(a):
    res=[0]*mx_bit
    for x in a:
        for i in range(mx_bit-1,-1,-1):
            if x>>i&1:
                if res[i]:
                    x^=res[i]
                else:
                    res[i]=x
                    break
    return res
def baseinsert(b,x):
    for i in range(mx_bit-1,-1,-1):
        if x>>i&1:
            if b[i]:
                x^=b[i]
            else:
                b[i]=x
                return True   
    return False