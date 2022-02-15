import random
class Brain:
    

    def getAction(self, boardState, agent):
        action = ()
        if agent == 0:
            # random agent turn
            moves = self.getMoves(boardState)
            movesLeft = len(moves)
            index = random.randint(0, movesLeft - 1)
            action = moves[index]
        elif agent == 1:
            # reflex agent turn
            moves = self.getMoves(boardState)

            scores = [self.reflexEvaluationFunction(boardState, action) for action in moves]
            print(scores)
            bestScore = max(scores)
            bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
            chosenIndex = random.choice(bestIndices) # Pick randomly among the best

            action = moves[chosenIndex]

        elif agent == 2:
            # minimax agent turn

            def minimax(boardState, depth, alpha, beta, agent):
                if depth == 0 or self.isLose(boardState) or self.isWin(boardState):
                    if self.isWin(boardState):
                        return float("inf")
                    elif self.isLose(boardState):
                        return float("-inf")
                    return self.evaluationFunction(boardState)

                if agent == -1:
                    maxEval = float("-inf")
                    for move in self.getMoves(boardState):
                        eval = minimax(self.generateSuccessor(boardState, -1, move), depth - 1, alpha, beta, -agent)
                        maxEval = max(maxEval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
                    print(maxEval)
                    return maxEval
                else:
                    minEval = float("inf")
                    for move in self.getMoves(boardState):
                        eval = minimax(self.generateSuccessor(boardState, 1, move), depth - 1, alpha, beta, -agent)
                        minEval = min(minEval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                    return minEval

            a = float("-inf")
            b = float("inf")
            for move in self.getMoves(boardState):
                utility = minimax(self.generateSuccessor(boardState, -1, move), 9, a, b, 1)
                if utility > a:
                    a = utility
                    action = move

        return action

    def reflexEvaluationFunction(self, boardState, move):
        print(boardState)

        nextState = self.generateSuccessor(boardState, -1, move)

        if self.isWin(nextState):
            return float("inf")
        
        # can never happen
        if self.isLose(nextState):
            return float("-inf")

        # need to check if can block a line with two O's already in it
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
            ]
        loseLines = []
        for line in lines:
            totalO = 0
            totalX = 0
            for x, y in line:
                if boardState[x][y] == -1:
                    totalX += 1
                elif boardState[x][y] == 1:
                    totalO += 1
            if totalO == 2 and totalX == 0:
                loseLines.append(line)
        
        for line in loseLines:
            for x, y in line:
                if boardState[x][y] == 0:
                    if (x, y) == move:
                        return float("inf") - 100
        # if the current move DOES block the win state, do block and return a high score
        # but a little less than a win move

        return 0


    def evaluationFunction(self, boardState):
        score = 0
        playerScore = 0
        computerScore = 0
        """
            the state is evaluated based on how many X's/O'x are in a line
            - +10 for 1 X, +100 for 2 X, +1000 for 3 X
            - -10 for 1 O, -100 for 2 O, -1000 for 3 O
        """

        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
            ]
        for line in lines:
            totalO = 0
            totalX = 0
            for x, y in line:
                if boardState[x][y] == -1:
                    totalX += 1
                elif boardState[x][y] == 1:
                    totalO += 1
            playerScore -= (10 ** (totalO - 1))
            computerScore += (10 ** (totalX - 1))
        
        score = computerScore + playerScore
        return score

    def isWin(self, board):
        winStates = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]
        if [-1, -1, -1] in winStates:
            return True
        return False

    def isLose(self, board):
        winStates = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]

        if [1, 1, 1] in winStates:
            return True
        return False

    def getMoves(self, boardState):
        legalMoves = []
        for row in range(3):
            for col in range(3):
                if boardState[row][col] == 0:
                    legalMoves.append((row, col))
        return legalMoves

    def generateSuccessor(self, boardState, agent, action):
        # returns the successor board after agent takes a turn
        newBoard = [[0,0,0], [0,0,0], [0,0,0]]
        for row in range(3):
            for col in range(3):
                if boardState[row][col] == -1:
                    newBoard[row][col] = -1
                elif boardState[row][col] == 1:
                    newBoard[row][col] = 1
        newBoard[action[1]][action[0]] = agent
        print(newBoard)
        return newBoard
