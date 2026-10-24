# Runtime: 17 ms
# Memory: 12.2 MB


class Solution(object):
    def isValidSudoku(self, board):

        def check(r, c):
            num = board[r][c]

            # Check row
            for j in range(9):
                if j != c and board[r][j] == num:
                    return False

            # Check column
            for i in range(9):
                if i != r and board[i][c] == num:
                    return False

            # Find top-left corner of the 3x3 box
            box_row = (r // 3) * 3
            box_col = (c // 3) * 3

            # Check 3x3 box
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if (i != r or j != c) and board[i][j] == num:
                        return False

            return True

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if not check(r, c):
                    return False

        return True
