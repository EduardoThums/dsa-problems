from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_with_the_greatest_number_of_candies = 0

        for kid in candies:
            if kid > kid_with_the_greatest_number_of_candies:
                kid_with_the_greatest_number_of_candies = kid

        return [kid + extraCandies >= kid_with_the_greatest_number_of_candies for kid in candies]


if __name__ == '__main__':
    i1 = [12,1,12]
    i2 = 10

    print(Solution().kidsWithCandies(i1, i2))
