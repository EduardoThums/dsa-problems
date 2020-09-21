from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator = 0

        output = []

        for num in nums:
            accumulator += num

            output.append(accumulator)

        return output

if __name__ == '__main__':
    arr = [1,1,1,1,1]

    print(Solution().runningSum(arr))