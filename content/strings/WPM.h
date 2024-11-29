/** 
 * Author: X
 * Description: Wildcard Pattern Matching
 * Given strings S and T consisting of lowercase English letters and
 * asterisks (*) wildcards, returns W where W[i] = 1 iff $S[i:i+|T|]$
 * and T are matched, 0 otherwise
 * S : abc*b*a***a, T : *b*a, W : 10111011
 * Time: approx. $O(N)$
*/

#include <tr2/dynamic_bitset>
using namespace std::tr2;
void WPM(string s, string t){
    nt n = s.length(), m = t.length();
    vector<dynamic_bitset<>> b(26, dynamic_bitset<>(n));
    for(int i = 0; i < n; i ++){
        if(s[i] != '*')
            b[s[i] - 'a'][i] = true;
        else
            for(int c = 0; c < 26; c ++)
                b[c][i] = true;
    }
    vector<int> shift(26, 0);
    dynamic_bitset<> good(n);
    good.set();
    for(int i = 0; i < m; i ++){
        if(t[i] == '*') continue;
        b[t[i] - 'a'] >>= (i - shift[t[i] - 'a']);
        shift[t[i] - 'a'] = i;
        good &= (b[t[i] - 'a']);
    }
    for(int i = 0; i < n - m + 1; i ++)
        cout << good[i];
    cout << endl;
}
