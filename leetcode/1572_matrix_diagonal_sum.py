from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        left_index = 0
        right_index = len(mat) - 1

        for l in mat:
            if left_index == right_index:
                total += l[left_index]

            else:
                total += l[left_index] + l[right_index]

            left_index += 1
            right_index -= 1

        return total
