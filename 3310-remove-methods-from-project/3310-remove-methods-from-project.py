class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        suspicious = set()
        q = deque([k])
        while q:
            node = q.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in graph[node]:
                if nei not in suspicious:
                    q.append(nei)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        return [i for i in range(n) if i not in suspicious]

        