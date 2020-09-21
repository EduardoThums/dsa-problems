class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0

        for a in J:

            for b in S:

                if a == b:
                    count += 1

        return count