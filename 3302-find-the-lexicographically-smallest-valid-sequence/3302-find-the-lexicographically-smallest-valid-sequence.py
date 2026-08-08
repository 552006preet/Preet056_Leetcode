class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        prefix = [0] * (n+1)
        j = 0
        for i in range(n):
            if j < m and word1[i] == word2[j]:
                j += 1
            prefix[i+1] = j
        suffix = [0] * (n+1)
        j = 0
        for i in range(n-1, -1, -1):
            if j < m and word1[i] == word2[m-j-1]:
                j += 1
            suffix[i] = j

        res, j, mismatch = [], 0, False
        for i in range(n):
            if j == m: break
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not mismatch and suffix[i+1] >= m-j-1:
                res.append(i)
                j += 1
                mismatch = True

        return res if j == m else []
