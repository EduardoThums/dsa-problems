from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_part = nums[0: n]
        result = []

        for index, num in enumerate(first_part):
            result.append(num)
            result.append(nums[index + n])

        return result


if __name__ == '__main__':
    arr = [2,5,1,3,4,7]

    print(Solution().shuffle(arr, 3))
