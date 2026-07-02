class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we can use a heap for this question
        # A min-heap always gives you the smallest element first
        # If we insert every point into a min-heap, using its squared distance from the origin as the priority
        # The closest point will be at the top
        # The next closest will be removed next, and so on

        minHeap = []

        # build our heap
        for x, y in points:
            # compute the distance
            dist = (x**2) + (y **2)

            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        result = []

        while k> 0:
            dist, x, y = heapq.heappop(minHeap)

            result.append([x,y])
            k -= 1
        

        return result