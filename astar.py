from puzzle import Puzzle
from math import sqrt


class Astar:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        h1 = self.h1
        h2 = self.h2
        h3 = self.h3
        g = self.g

    def f1(self):
        """
        return estimated total cost 
        of cheapest solution for h1
        """
        return self.heuristic1 + self.g

    def f2(self):
        return self.heuristic2 + self.g

    def f3(self):
        return self.h3 + self.g

    def heuristic1(self):
        """
        misplaced tiles
        """
        count = 0
        board = self.puzzle.board
        goalstate = self.puzzle.puzzleEndState(self.puzzle.size)
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                if ((board[i][j] != goalstate[i][j]) and board[i][j] != 0):
                    count += 1

        return count

    def heuristic2(self):
        """
        manhattan distance
        """
        distance = 0
        board = self.puzzle.board
        size = self.puzzle.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (self.puzzle.board[i][j]-1)//size  #
                    y = (self.puzzle.board[i][j]-1) % size  #
                    distance += abs(x-i)+abs(y-j)  # 0
        return distance

    def heuristic3(self):

        distance = 0
        board = self.puzzle.board
        size = self.puzzle.size
        goalstate = self.puzzle.puzzleEndState(self.puzzle.size)

        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (self.puzzle.board[i][j]-1)//size  #
                    y = (self.puzzle.board[i][j]-1) % size  #
                    distance += sqrt((x-i)**2 + (y-j)**2)

        return distance
