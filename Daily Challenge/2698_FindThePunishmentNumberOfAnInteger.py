'''
Approach
- Iterate through numbers 1 to n.
- Compute the square of each number.
- Use recursion to check if the square can be partitioned into contiguous substrings summing to the original number.
- If a valid partition exists, add the square to the total res.
- Return the accumulated res as the punishment number of n.

Complexity
Time complexity: Best Case: O(nlogn), Worst Case: O(n^2)
Space complexity: O(logn)
'''

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def partition(i, cur: int, target: int, string: str):
            if i == len(string) and cur == target:
                return True

            for j in range(i, len(string)):
                string[i: j+1]
                if partition(j+1, cur + int(string[i: j+1]), target, string):
                    return True
            return False
        
        res = 0
        for i in range(1, n+1):
            if partition(0, 0, i, str(i*i)):
                res += i*i
        return res