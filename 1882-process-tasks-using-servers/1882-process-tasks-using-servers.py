import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    _, w, idx = heapq.heappop(busy)
                    heapq.heappush(available, (w, idx))

            w, idx = heapq.heappop(available)
            ans.append(idx)

            heapq.heappush(busy, (time + task, w, idx))

        return ans