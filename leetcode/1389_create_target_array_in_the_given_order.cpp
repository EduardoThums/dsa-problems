#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void print(vector<int> const& input) {
    for (int i = 0; i < input.size(); i++) {
        cout << input.at(i) << ' ';
    }
}

class Solution {
   public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> target;

        for (int i = 0; i < index.size(); i++) {
            target.insert(target.begin() + index[i], nums[i]);
        }

        return target;
    }
};

int main() {
    Solution solution;

    vector<int> nums{0, 1, 2, 3, 4};
    vector<int> index{0, 1, 2, 2, 1};

    print(solution.createTargetArray(nums, index));

    return 0;
}