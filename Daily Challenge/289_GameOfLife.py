'''
Approach:
- Iteration 1: Iterate through the board to determine the next state of each cell.
    - Count live neighbors using an 8-directional lookup.
    - Apply Game of Life rules while modifying the board in-place.
    - Since we have to make changes in-place, use encoding: -1 for live-to-dead and 2 for dead-to-live transitions.
- Iteration 2: Update -1 → 0 and 2 → 1 for final transformation.

Complexity:
Time complexity: O(m∗n)
Space complexity: O(1)
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                freq = defaultdict(int)
                neighbors = [[r, c-1], [r, c+1], [r-1, c], [r+1, c], [r-1, c-1], [r-1, c+1], [r+1, c-1], [r+1, c+1]]

                for nr, nc in neighbors:
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if board[nr][nc] == 2:
                            freq[0] += 1
                        elif board[nr][nc] == -1:
                            freq[1] += 1
                        else:
                            freq[board[nr][nc]] += 1
                if board[r][c] == 1:
                    if freq[1] < 2:
                        board[r][c] = -1
                    elif freq[1] > 3:
                        board[r][c] = -1
                elif board[r][c] == 0:
                    if freq[1] == 3:
                        board[r][c] = 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0