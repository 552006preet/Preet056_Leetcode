class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen=defaultdict(list)

        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            seen[tuple(count)].append(i)
        return list(seen.values())