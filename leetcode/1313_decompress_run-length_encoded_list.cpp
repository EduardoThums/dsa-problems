#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> out;

        for (int i = 0; i < nums.size(); i += 2) {
            for (int j = 0; j < nums[i]; j++) {
                out.push_back(nums[i + 1]);
            }
        }

        return out;
    }
};

void print(vector<int> const& input) {
    for (int i = 0; i < input.size(); i++) {
        cout << input.at(i) << ' ';
    }
}

int main() {
    Solution solution;

    vector<int> nums{1, 2, 3, 4};

    print(solution.decompressRLElist(nums));

    return 0;
}