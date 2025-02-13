'''
Approach:
- Convert nums into a minHeap
- While nums[0] is less than k:
    - Increment operations variable
    - Calculate: new = heappop(nums) * 2 + heappop(nums)
    - Push new element to nums
- Return operations

Complexity:
- Time complexity: O(NlogN)
- Space complexity: O(N)

'''
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        heapify(nums)
        while nums[0] < k:
            operations += 1
            new = heappop(nums) * 2 + heappop(nums)
            heappush(nums, new)
        return operations