class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def yesity(board, word, i , j):
            if word == "":
                return True
            
            
            if "bubba" == board[i][j]:
                if i>0:
                    if word[0] == board[i-1][j]:
                        temp = board[i][j]
                        board[i][j] = "bobbity"
                        temp2 = board[i-1][j]
                        board[i-1][j] = "bubba"
                        splitity = word[1:]
                        if yesity(board, splitity, i-1, j):
                            return True
                        board[i][j] = temp
                        board[i-1][j] = temp2

                if i<len(board)-1:
                    if word[0] == board[i+1][j]:
                        temp = board[i][j]
                        board[i][j] = "bobbity"
                        temp2 = board[i+1][j]
                        board[i+1][j] = "bubba"
                        splitity = word[1:]
                        if yesity(board, splitity, i+1, j):
                            return True
                        board[i][j] = temp
                        board[i+1][j] = temp2
                if j>0:
                    if word[0] == board[i][j-1]:
                        temp = board[i][j]
                        board[i][j] = "bobbity"
                        temp2 = board[i][j-1]
                        board[i][j-1] = "bubba"
                        splitity = word[1:]
                        if yesity(board, splitity, i, j-1):
                            return True
                        board[i][j] = temp
                        board[i][j-1] = temp2
                if j<len(board[0])-1:
                    if word[0] == board[i][j+1]:
                        temp = board[i][j]
                        board[i][j] = "bobbity"
                        temp2 = board[i][j+1]
                        board[i][j+1] = "bubba"
                        splitity = word[1:]
                        if yesity(board, splitity, i, j+1):
                            return True
                        board[i][j] = temp
                        board[i][j+1] = temp2

            return False
                        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    temp = board[i][j]
                    board[i][j] = "bubba"
                    splifity = word[1:]
                    if yesity(board, splifity, i, j):
                        return True
                    board[i][j] = temp
        return False