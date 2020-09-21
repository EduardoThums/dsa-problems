from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, num in enumerate(nums):
            values[num] = index

        for index, num in enumerate(nums):
            to_find = target - num
            if to_find in values and index != values[to_find]:
                return [index, values[to_find]]
