class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        vector<char> mapStoT(256,1);
        vector<char> mapTtoS(256,1);

        for (int i = 0; i < t.size(); i++){
            char a = s[i];
            char b = t[i];

            if (mapStoT[a] != 1 and mapStoT[a] != b) return false;
            if (mapTtoS[b] != 1 and mapTtoS[b] != a) return false;

            mapStoT[a] = b;
            mapTtoS[b] = a;
        }

        return true;

    }
};
