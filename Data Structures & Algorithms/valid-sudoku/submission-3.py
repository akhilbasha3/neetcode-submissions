class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                num = board[r][c]

                row = (r, num)
                col = (c, num)
                box = (r // 3, c // 3, num)

                if row in rows or col in cols or box in boxes:
                    return False

                rows.add(row)
                cols.add(col)
                boxes.add(box)

        return True
