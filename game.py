import brain

class TicTacToe:
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    computer = brain.Brain()

    turn = 1

    def __init__(self, agent):
        """ AGENT IS DETERMINED BY #
            0 = randomAgent
            1 = reflexAgent
            2 = minimaxAgent
        """
        self.agent = agent
        self.updateWinStates()
        
    def getBoard(self):
        return self.board

    def doTurn(self, row, col):
        if self.board[row][col] == 0:
            if self.turn == 1:
                self.playerTurn(row, col)
                if self.isWin() != 1 and self.movesLeft() != 0:
                    self.computerTurn()
            return True
        else:
            return False

    def playerTurn(self, row, col):
        self.turn = -1
        self.board[row][col] = 1

    def computerTurn(self):
        self.turn = 1
        newBoard = [[0,0,0], [0,0,0], [0,0,0]]
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == -1:
                    newBoard[row][col] = -1
                elif self.board[row][col] == 1:
                    newBoard[row][col] = 1
        action = self.computer.getAction(self.board, self.agent)
        newBoard[action[0]][action[1]] = -1
        self.board = newBoard

    def isWin(self):
        self.updateWinStates()
        if [1, 1, 1] in self.winStates:
            return 1
        elif [-1, -1, -1] in self.winStates:
            return -1
        else:
            return 0
    
    def updateWinStates(self):
        self.winStates = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]]
        ]
    
    def movesLeft(self):
        count = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    count += 1
        return count
