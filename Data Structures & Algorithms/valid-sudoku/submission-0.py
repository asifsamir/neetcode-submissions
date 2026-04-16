class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        box_dict = collections.defaultdict(set)
        

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                current_num = board[row][col]
                if current_num in row_dict[row] or current_num in col_dict[col] or current_num in box_dict[(row//3, col//3)]:
                    return False
                else:
                    row_dict[row].add(current_num)
                    col_dict[col].add(current_num)
                    box_dict[(row//3, col//3)].add(current_num)

        return True



        


        