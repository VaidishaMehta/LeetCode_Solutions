'''
Approach:
- Compute the digit sum for each number in nums.
- Group numbers that have the same digit sum using a hash map.
- Use a max heap to efficiently retrieve the two largest numbers in each group.
- Return the maximum sum of such a pair, or -1 if no valid pair exists.

Complexity:
- Time complexity: O(NlogN)
- Space complexity: O(N)

'''
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumOfDigits = [0] * len(nums)
        freq = defaultdict(list)
        for i in range(len(nums)):
            curr = nums[i]
            while curr != 0:
                sumOfDigits[i] += curr % 10
                curr = curr // 10
            heapq.heappush(freq[sumOfDigits[i]], -nums[i])
        res = -1
        for v in freq.values():
            if len(v) > 1:
                res = max(-(heapq.heappop(v) + heapq.heappop(v)), res)
        return res