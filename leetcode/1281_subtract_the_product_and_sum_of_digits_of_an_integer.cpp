#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0;

        while (n > 0) {
            product *= n % 10;
            sum += n % 10;

            n /= 10;
        }

        return product - sum;
    }
};

void print(vector<int> const& input) {
    for (int i = 0; i < input.size(); i++) {
        cout << input.at(i) << ' ';
    }
}

int main() {
    Solution solution;

    int n;

    cin >> n;

    cout << solution.subtractProductAndSum(n);

    return 0;
}