class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm_row = defaultdict(set);
        hm_col = defaultdict(set);
        hm_box = defaultdict(set);

        col_count = 0;
        repeated = False;

        for i in range(9):
            for j in range(9):
                #check row
                if board[j][i] in hm_col[i]:
                    return False;
                if board[i][j] in hm_row[i]:
                    return False;
                if board[i][j] in hm_box[(i // 3) * 3 + (j // 3)]:
                    return False;
                # else:
                if board[i][j] != ".":
                    hm_row[i].add(board[i][j]);
                    hm_box[(i // 3) * 3 + (j // 3)].add(board[i][j]);
                if board[j][i] != ".":
                    hm_col[i].add(board[j][i]);

        return True;

# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]
