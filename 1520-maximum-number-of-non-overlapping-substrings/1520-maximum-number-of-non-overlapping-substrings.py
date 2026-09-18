class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last index of each character
        first = {ch: i for i, ch in reversed(list(enumerate(s)))}
        last = {ch: i for i, ch in enumerate(s)}

        valid_intervals = []

        # Step 2: Expand range for each character's first occurrence
        for ch in set(s):
            left = first[ch]
            right = last[ch]

            is_valid = True
            i = left
            while i <= right:
                # If a character inside has an earlier start index than 'left',
                # this substring cannot start at 'left' (it would be invalid/non-minimal).
                if first[s[i]] < left:
                    is_valid = False
                    break
                # Expand right boundary to include all occurrences of s[i]
                right = max(right, last[s[i]])
                i += 1

            if is_valid:
                valid_intervals.append((right, left))

        # Step 3: Sort by ending index and greedily select non-overlapping substrings
        valid_intervals.sort()

        ans = []
        prev_end = -1
        for right, left in valid_intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans