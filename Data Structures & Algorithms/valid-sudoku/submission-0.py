class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                if val in row[r]:
                    return False
                row[r].add(val)

                if val in col[c]:
                    return False
                col[c].add(val)

                box = (r // 3, c // 3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)

        return True            