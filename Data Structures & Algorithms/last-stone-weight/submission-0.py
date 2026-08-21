import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        h = stones
        while len(h) > 1:
            a = -1 * heapq.heappop(h)
            b = -1 * heapq.heappop(h)
            if a != b:
                heapq.heappush(h,min(a-b,b-a))
        if len(h) == 0:
            return 0
        return -1 * stones[0]