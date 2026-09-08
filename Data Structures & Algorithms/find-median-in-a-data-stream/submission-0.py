class MedianFinder:
    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.large_heap and num > self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -num)

        if len(self.large_heap) > len(self.small_heap) + 1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap,-val)

        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        median =  (-1 * self.small_heap[0] + self.large_heap[0]) / 2.0
        return median
        