'''
Approach:
- Iterate through thepatternwhile pushing numbers (1 to n+1) into thestack.
- If an'I'is encountered or at the end of the pattern, pop all elements from thestackand add them to the resultres.
- This ensures'D'sequences are stored in thestack(maintaining decreasing order) and resolved when an'I'appears or when we have reached end of thepattern.
- The result is built by popping from thestack, ensuring the lexicographically smallest valid number.
- Finally, the resultresis returned as a string.

Complexity:
Time complexity:O(N)
Space complexity:O(N)
'''

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i in range(len(pattern)+1):
            stack.append(i+1)
            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
        
        return ''.join(res)