class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we can use a heap for this question

        minHeap = []

        # build our heap
        for x, y in points:
            dist = (x**2) + (y **2)

            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        result = []

        while k> 0:
            dist, x, y = heapq.heappop(minHeap)

            result.append([x,y])
            k -= 1
        

        return result