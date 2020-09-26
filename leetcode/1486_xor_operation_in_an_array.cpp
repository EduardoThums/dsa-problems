#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int xorOperation(int n, int start) {
        int out = start;

        for (int i = 1; i<n; i++ ){
            out ^= start + (i * 2);
        }

        return out;
    }
};

int main() {
    int n, start;

    cin >> n >> start;

    Solution solution;

    cout << solution.xorOperation(n, start);

    return 0;
}