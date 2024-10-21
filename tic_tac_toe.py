import os
import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 17
        self.playerLetter = ''
        self.computerLetter = ''

    def drawBoard(self):
        print(self.board[13] + ' | ' + self.board[14] + '| ' + self.board[15] + '| ' + self.board[16])
        print('--+--+--+--')
        print(self.board[9] + ' | ' + self.board[10] + '| ' + self.board[11] + '| ' + self.board[12])
        print('--+--+--+--')
        print(self.board[5] + ' | ' + self.board[6] + '| ' + self.board[7] + '| ' + self.board[8])
        print('--+--+--+--')
        print(self.board[1] + ' | ' + self.board[2] + '| ' + self.board[3] + '| ' + self.board[4])

    def inputPlayerLetter(self):
        letter = ''
        while letter not in ['X', 'O']:
            print("=" * 40)
            letter = input("Do you want to be X or O?: ").upper()
        self.playerLetter, self.computerLetter = (['X', 'O'] if letter == 'X' else ['O', 'X'])

    def whoGoesFirst(self):
        return 'computer' if random.randint(0, 1) == 0 else 'player'

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
        bo = self.board
        return (
            # diagonals
            (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le) or
            (bo[13] == le and bo[10] == le and bo[7] == le and bo[4] == le) or
            # rows
            (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
            (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
            (bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or
            # columns
            (bo[1] == le and bo[5] == le and bo[9] == le and bo[13] == le) or
            (bo[2] == le and bo[6] == le and bo[10] == le and bo[14] == le) or
            (bo[3] == le and bo[7] == le and bo[11] == le and bo[15] == le) or
            (bo[4] == le and bo[8] == le and bo[12] == le and bo[16] == le)
        )

    def getBoardCopy(self):
        return self.board.copy()

    def isSpaceFree(self, move):
        return self.board[move] == ' '

    def getPlayerMove(self):
        move = ' '
        while move not in map(str, range(1, 17)) or not self.isSpaceFree(int(move)):
            if move in map(str, range(1, 17)):
                print("=" * 40)
                print("Space already have item")
            print("=" * 40)
            print('What is your next move? (1-16)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, movesList):
        possibleMoves = [i for i in movesList if self.isSpaceFree(i)]
        return random.choice(possibleMoves) if possibleMoves else None

    def getComputerMove(self):
        # Check if computer can win
        for i in range(1, 17):
            boardCopy = self.getBoardCopy()
            if self.isSpaceFree(i):
                self.makeMove(self.computerLetter, i)
                if self.isWinner(self.computerLetter):
                    return i
                self.board = boardCopy

        # Check if player can win and block them
        for i in range(1, 17):
            boardCopy = self.getBoardCopy()
            if self.isSpaceFree(i):
                self.makeMove(self.playerLetter, i)
                if self.isWinner(self.playerLetter):
                    return i
                self.board = boardCopy

        # Try to take corners
        move = self.chooseRandomMoveFromList([1, 4, 13, 16])
        if move is not None:
            return move

        # Try to take center squares
        if self.isSpaceFree(10) and self.isSpaceFree(11):
            return 10

        # Take any other available move
        return self.chooseRandomMoveFromList([2, 3, 5, 8, 9, 12, 14, 15])

    def isBoardFull(self):
        return all(not self.isSpaceFree(i) for i in range(1, 17))

    def playGame(self):
        print('======Welcome to Tic-Tac-Toe Game!======')
        while True:
            self.board = [' '] * 17
            self.inputPlayerLetter()
            turn = self.whoGoesFirst()
            print("=" * 40)
            print('The ' + turn + ' will go first.')

            while True:
                if turn == 'player':
                    self.drawBoard()
                    move = self.getPlayerMove()
                    self.makeMove(self.playerLetter, move)

                    if self.isWinner(self.playerLetter):
                        self.drawBoard()
                        print("=" * 40)
                        print('Hooray! You have won the game!')
                        break
                    else:
                        if self.isBoardFull():
                            self.drawBoard()
                            print("=" * 40)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'computer'
                else:
                    move = self.getComputerMove()
                    self.makeMove(self.computerLetter, move)
                    if self.isWinner(self.computerLetter):
                        self.drawBoard()
                        print("=" * 40)
                        print('The computer has beaten you! You lose.')
                        break
                    else:
                        if self.isBoardFull():
                            self.drawBoard()
                            print("=" * 40)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'
            print("=" * 40)
            playAgain = input('Do you want to play again? (y/n): ').lower()
            if playAgain == "n":
                break
