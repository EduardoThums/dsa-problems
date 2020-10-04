from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        index = 0

        for x, y in points[:-1]:
            seconds += max(abs(points[index + 1][0] - x), abs(points[index + 1][1] - y))
            index += 1

        return seconds
