#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    int balancedStringSplit(string s) {
        int c = 0, l = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'L') {
                l++;
            } else {
                l--;
            }

            if (l == 0) {
                c++;
            }
        }

        return c;
    }
};

int main() {
    string s;

    cin >> s;

    Solution solution;

    cout << solution.balancedStringSplit(s);

    return 0;
}