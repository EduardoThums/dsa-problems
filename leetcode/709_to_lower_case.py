from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        init_x, init_y = points[0]

        for point in points[1:]:
            final_x, final_y = point

            while init_x != final_x and init_y != final_y:
                if final_x > init_x:
                    init_x += 1

                if final_y > init_y:
                    init_y += 1

                if final_x < init_x:
                    init_x -= 1

                if final_y < init_y:
                    init_y -= 1

                seconds += 1

            if init_x == final_x and init_y == final_y:
                seconds += 1

            init_x, init_y = final_x, final_y

        return seconds


if __name__ == '__main__':
    points = [[3, 2], [-2, 2]]

    print(Solution().minTimeToVisitAllPoints(points))
