'''
Approach:
- Calculate distance: For each point (x, y), compute its squared Euclidean distance dist = x^2 + y^2.
- Store distance and point: Append a tuple (dist, (x, y)) to the distance list.
- Heapify: Use heapq.heapify(distance) to convert the distance list into a valid min-heap.
- Extract k closest points: For k iterations, pop the smallest element from the heap using heappop(), which gives the point (x, y) and append it to ans.
- Return result: Return the ans list containing the k closest points.

Complexity:
- Time complexity: O(n+klogn)
- Space complexity: O(n)
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distance = []
        for x, y in points:
            dist = x**2 + y**2
            distance.append((dist, (x, y))) #we append to the distance array here instead of heappush() as append() takes O(1) time while heappush() takes O(log n) time
        heapq.heapify(distance) #O(n)
        for i in range(k):
            ans.append(heapq.heappop(distance)[1]) #O(logn)
        return ans