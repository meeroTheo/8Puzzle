import random
from math import sqrt


class Puzzle:

    def __init__(self, size,new):

        # n x n size of puzzle 3,4,5(8,15,24)
        self.size = int((size+1) ** (1/2))
        self.board = [[0 for x in range(self.size)]
                      for y in range(self.size)]  # matrix
        self.new=new
        if (new):
            solvable = self.createP()
            while (not solvable):
                solvable = self.createP()
            self.h1 = self.heuristic1()
            self.h2 = self.heuristic2()
            self.h3 = self.heuristic3()

    def createP(self):
        list = random.sample(range(self.size**2), self.size**2)

        index = 0
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = list[index]
                index += 1
                
        self.h1 = self.heuristic1()
        self.h2 = self.heuristic2()
        self.h3 = self.heuristic3()
        return self.isSolvable(self.board,(self.size**2))

    def setBoard(self):
        self.h1 = self.heuristic1()
        self.h2 = self.heuristic2()
        self.h3 = self.heuristic3()
        return

    def set_h2(self):
        self.h2 = self.heuristic2()
        return

    def set_h1(self):
        self.h1 = self.heuristic1()
        return

    def set_h3(self):
        self.h3 = self.heuristic3()
        return

    def puzzleEndState(self):
        """
        Predetermined goal state for puzzles

        """
        if self.size == 3:
            puzzleEndState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif self.size == 4:
            puzzleEndState = [[1, 2, 3, 4], [5, 6, 7, 8],
                              [9, 10, 11, 12], [13, 14, 15, 0]]
        else:  # 24 puzzle
            puzzleEndState = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
                11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        return puzzleEndState

    def __str__(self) -> str:
        str= ""
        puzzle_len = self.size
        if puzzle_len == 3:
            for row in self.board:
                str += "{: >5} {: >5} {: >5}\n".format(*row)
        elif puzzle_len == 4:
            for row in self.board:
                str += "{: >5} {: >5} {: >5} {: > 5}\n".format(*row)
        else:  # if puzzle size is 24 (5)
            for row in self.board:
                str += "{: >5} {: >5} {: >5} {: >5} {: >5}\n".format(*row)
        str+="---------------"
        return str

    def solved(self):
        """
        If board is in increasing order,
        and 0 is on last value of matrix,
        puzzle is solved
        """
        return (self.board == self.puzzleEndState())

    def calDP(self,puz, size):
        dp = 0
        for i in range(0, size):
            for j in range(i + 1, size):
                if puz[j] != 0 and puz[i] != 0 and puz[i] > puz[j]:
                    dp += 1
        return dp
 
    def isSolvable(self,puzzle,size) :
        """
        Determines the disorder parameter
        Determines if the puzzle is solvable (DP even)

        even = true
        """
        # Count inversions in given 8 puzzle
        dp = self.calDP([j for sub in puzzle for j in sub],size)
    
        # return true if dp is even.
        return (dp % 2 == 0)

    def heuristic1(self):
        """
        misplaced tiles
        """
        count = 0
        board = self.board
        goalstate = self.puzzleEndState()
        for i in range(self.size):
            for j in range(self.size):
                if ((board[i][j] != goalstate[i][j]) and board[i][j] != 0):
                    count += 1
        return count

    def heuristic2(self):
        """
        manhattan distance
        """
        distance = 0
        board = self.board
        size = self.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += abs(x-i)+abs(y-j)  # 0
        return distance

    def heuristic3(self):
        distance = 0
        board = self.board
        size = self.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += sqrt((x-i)**2 + (y-j)**2)

        return distance

    def deepcopy(self):

        temp = Puzzle(((self.size) ** 2)-1,False)
        temp.new=True

        for i in range(self.size):
            for j in range(self.size):
                temp.board[i][j] = self.board[i][j]
        temp.setBoard()
        return temp

    def isEqual(self, puzzle):
        equal = True
        if (self.size == puzzle.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] != puzzle.board[i][j]:
                        equal = False
        else:
            equal = False
        return equal

    def moves(self, x1, y1, x2, y2):
        """
        Gets the state of an adjacent node
        which we swap with the 0
        Returns the new state
        """
        # check if the move is valid
        if x2 >= self.size or x2 < 0 or y2 >= self.size or y2 < 0:
            return None
        # swap the 0 with the adjacent node
        tempState = self.deepcopy()
        tempVal = tempState.board[x2][y2]
        tempState.board[x2][y2] = tempState.board[x1][y1]

        tempState.board[x1][y1] = tempVal
        return tempState
