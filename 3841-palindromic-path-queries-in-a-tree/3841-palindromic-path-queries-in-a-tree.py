class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(g[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Correct preorder: use an explicit enter/exit traversal
        # Rebuild the Euler order and subtree ranges.
        timer = 0
        stack = [(0, -1, False)]
        while stack:
            u, p, exiting = stack.pop()
            if exiting:
                tout[u] = timer
                continue

            tin[u] = timer
            timer += 1
            stack.append((u, p, True))
            for v in reversed(g[u]):
                if v != p:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        LOG = n.bit_length()
        up = [parent[:]]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u, v = up[j][u], up[j][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_xor(l, r, x):
            add(l, x)
            if r < n:
                add(r, x)

        def mask(c):
            return 1 << (ord(c) - ord('a'))

        chars = list(s)
        for u in range(n):
            range_xor(tin[u], tout[u], mask(chars[u]))

        ans = []
        for q in queries:
            typ, a, b = q.split()
            a = int(a)

            if typ == "update":
                change = mask(chars[a]) ^ mask(b)
                range_xor(tin[a], tout[a], change)
                chars[a] = b
            else:
                b = int(b)
                w = lca(a, b)
                x = prefix(tin[a]) ^ prefix(tin[b]) ^ mask(chars[w])
                ans.append((x & (x - 1)) == 0)

        return ans