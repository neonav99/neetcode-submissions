class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1 and stones:
            first = abs(heapq.heappop(stones))
            second = abs (heapq.heappop(stones))

            if first != second:
                diff = abs(first-second)
                heapq.heappush(stones,-diff)
        
        return -stones[0] if stones else 0

            
        