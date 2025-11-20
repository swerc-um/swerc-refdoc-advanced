/**
 * Author:
 * Description: On traite les poids du plus petit au plus grand en maintenant une liste initialement vide $W'$.
 * S'il y a $occ$ occurrences du plus petit poids $w$ :
 *  - Si $occ$ est impair : ajouter $(occ-1)/2$ occurrences de $2w$ aux poids, et une occurrence de $w$ à $W'$.
 *  - Si $occ$ est pair : ajouter $(occ-2)/2$ occurrences de $2w$ aux poids, et deux occurrences de $w$ à $W'$.
 * Time: $O(C \sqrt{C})$, où $\sum_{i=1}^{N} w_i = C$.
 */

