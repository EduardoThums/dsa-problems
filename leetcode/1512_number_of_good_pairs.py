from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        for index1, num1 in enumerate(nums):

            for index2, num2 in enumerate(nums):
                if num1 == num2 and index1 < index2:
                    good_pairs += 1

        return good_pairs

if __name__ == '__main__':
    i1 = [1,2,3,1,1,3]

    print(Solution().numIdenticalPairs(i1))