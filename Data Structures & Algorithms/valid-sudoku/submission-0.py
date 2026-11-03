class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for rowNum in range(9):
            row = set()
            for colNum in range(9):
                num = board[rowNum][colNum]
                if num == ".":
                    continue

                #row
                if num in row:
                    return False
                else:
                    row.add(num)

                #col
                if num in cols[colNum]:
                    return False
                else:
                    cols[colNum].add(num)

                #sub-box
                boxNum = (rowNum // 3) * 3 + (colNum // 3)
                if num in boxes[boxNum]:
                    return False
                else:
                    boxes[boxNum].add(num)
        
        return True