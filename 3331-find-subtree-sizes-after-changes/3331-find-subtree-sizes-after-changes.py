from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        last = [[] for _ in range(26)]
        ans = [1] * n
        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                last[c].append(node)
                stack.append((node, 1, parent[node]))

                for child in reversed(tree[node]):
                    stack.append((child, 0, node))

            else:
                target = prev

                if len(last[c]) > 1:
                    target = last[c][-2]

                if target != -1:
                    ans[target] += ans[node]

                last[c].pop()

        return ans