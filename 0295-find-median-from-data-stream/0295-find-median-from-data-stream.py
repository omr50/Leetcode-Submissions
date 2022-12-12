from heapq import heappush, heappop, heapify
class MedianFinder:

    def __init__(self):
        self.firstHeap, self.secondHeap = [], []
        # first heap will be a max heap and
        # the second heap will be a min heap
        heapify(self.firstHeap)
        heapify(self.secondHeap)
    def addNum(self, num: int) -> None:
         # -4 < 3 True
        # 4 < -3 False
        if not len(self.firstHeap) or num < -self.firstHeap[0]:
            heappush(self.firstHeap, -num)
        else:
            heappush(self.secondHeap, num)
        if abs(len(self.firstHeap) - len(self.secondHeap)) > 1:

            if len(self.firstHeap) > len(self.secondHeap):
                heappush(self.secondHeap, -heappop(self.firstHeap))
            else:
                heappush(self.firstHeap, -heappop(self.secondHeap))

    def findMedian(self) -> float:
        if (len(self.firstHeap) + len(self.secondHeap)) % 2 == 0:
            return (-self.firstHeap[0] + self.secondHeap[0])/2
        else:
            # print('odd')
            if len(self.firstHeap) > len(self.secondHeap):
                return -self.firstHeap[0]
            return self.secondHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()