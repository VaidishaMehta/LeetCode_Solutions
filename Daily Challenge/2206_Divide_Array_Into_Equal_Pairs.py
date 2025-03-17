'''
Approach
- Count the frequency of elements in nums.
- If frequency of any element is odd then return False, else return True.

Complexity
Time complexity: O(n)
Space complexity: O(n)
'''
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        
        for i in freq.values():
            if i & 1:
                return False
        return True