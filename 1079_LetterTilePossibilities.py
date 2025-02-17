'''
Approach:
- Use a Counter to store the frequency of each tile.
- Recursively generate all possible sequences by picking tiles.
- Increment res for each valid sequence formed.
- After recursion, restore the frequency for other combinations.
- Return the total count of valid sequences (res).

Complexity:
Time complexity: O(2^n)
Space complexity: O(n)
'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtracking():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtracking()
                    count[c] += 1
            return res
        return backtracking()