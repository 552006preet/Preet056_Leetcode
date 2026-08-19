from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for r, s in reservedSeats:
            reserved[r].add(s)

        result = 0
        for seats in reserved.values():
            # Check availability of the three blocks
            blockA = all(x not in seats for x in [2,3,4,5])
            blockB = all(x not in seats for x in [4,5,6,7])
            blockC = all(x not in seats for x in [6,7,8,9])

            if blockA and blockC:
                result += 2
            elif blockA or blockB or blockC:
                result += 1
            # else → 0 groups

        # Rows without reservations can always fit 2 groups
        result += (n - len(reserved)) * 2
        return result
       