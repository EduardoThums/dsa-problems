#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    string restoreString(string s, vector<int> &indices) {
        string ss = s;

        for (int i = 0; i < s.size(); i++) {
            ss[indices[i]] = s[i];
        }

        return ss;
    }
};

int main() {
    Solution solution;

    string s = "codeleet";
    vector<int> ids{4, 5, 6, 7, 0, 2, 1, 3};

    cout << solution.restoreString(s, ids);

    return 0;
}