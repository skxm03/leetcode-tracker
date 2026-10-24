# Runtime: 4 ms
# Memory: 12.2 MB


# class Solution(object):
#     def isValidSudoku(self, board):

#         def check(r, c):
#             num = board[r][c]

#             # Check row
#             for j in range(9):
#                 if j != c and board[r][j] == num:
#                     return False

#             # Check column
#             for i in range(9):
#                 if i != r and board[i][c] == num:
#                     return False

#             # Find top-left corner of the 3x3 box
#             box_row = (r // 3) * 3
#             box_col = (c // 3) * 3

#             # Check 3x3 box
#             for i in range(box_row, box_row + 3):
#                 for j in range(box_col, box_col + 3):
#                     if (i != r or j != c) and board[i][j] == num:
#                         return False

#             return True

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue

#                 if not check(r, c):
#                     return False

#         return True


class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_index]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True
