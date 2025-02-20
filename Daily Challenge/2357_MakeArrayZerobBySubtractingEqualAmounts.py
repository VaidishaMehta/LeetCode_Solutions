'''
Approach:
- Use a set to track unique non-zero elements in nums.
- Remove 0 from the set(if present).
- The size of the remaining set gives the number of operations needed since each unique value corresponds to a subtraction step.

Complexity:
Time complexity:O(N)
Space complexity:O(N)
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})