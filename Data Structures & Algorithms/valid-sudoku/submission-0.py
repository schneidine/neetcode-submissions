from collections import defaultdict
# Looked up solution, redo in future
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create dictionaries to validate each row and column
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        # Iterate through each row/column pair and
        # add to dict.

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                # skip if its a blank
                if cell == ".":
                    continue
                
                box = (r // 3, c // 3)

                # check if value is already found in its row or column
                if cell in rows[r] or cell in columns[c] or cell in boxes[box]:
                    return False

                # since its not in the row/column/box, add it to the dict
                rows[r].add(cell)
                columns[c].add(cell)
                boxes[box].add(cell)
            
        return True
