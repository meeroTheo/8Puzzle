import random


class Puzzle:

    def __init__(self, size):

        # n x n size of puzzle 3,4,5(8,15,24)
        self.size = int((size+1) ** (1/2))
        self.board = [[0 for x in range(self.size)]
                      for y in range(self.size)]  # matrix

        evenDP = self.createP()
        while (not evenDP):
            evenDP = self.createP()

    def createP(self):
        list = random.sample(range(self.size**2), self.size**2)
        print(list)
        index = 0
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = list[index]

                index += 1
        return self.isSolvable()

    def puzzleEndState(self, size):
        """
        Predetermined goal state for puzzles

        """
        if self.size == 8:
            puzzleEndState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif self.size == 15:
            puzzleEndState = [[1, 2, 3, 4], [5, 6, 7, 8],
                              [9, 10, 11, 12], [13, 14, 15, 0]]
        else:  # 24 puzzle
            puzzleEndState = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
                11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        return puzzleEndState

    def printPuzzle(self):
        """
        prints puzzle matrix with proper format
        """
        puzzle_len = self.size
        if puzzle_len == 3:
            for row in self.board:
                print("{: >5} {: >5} {: >5}".format(*row))
        elif puzzle_len == 4:
            for row in self.board:
                print("{: >5} {: >5} {: >5} {: > 5}".format(*row))

        else:  # if puzzle size is 24 (5)
            for row in self.board:
                print("{: >5} {: >5} {: >5} {: >5} {: >5}".format(*row))

        return

    def blank_position(puzzle):
      # iterate through all and return position of blank
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == 0:
                    return i, j

    def solved(self):
        """
        If board is in increasing order,
        and 0 is on last value of matrix,
        puzzle is solved
        """
        return (self.board == self.puzzleEndState(self.size))

    def isSolvable(self):
        """
        Determines the disorder parameter
        Determines if the puzzle is solvable (DP even)

        even = true
        """
        disorder = 0

        for i in range(self.size-1):
            for j in range(1+i, self.size-1):
                if (self.board[j][i] > 0) and (self.board[j][i] > self.board[i][j]):
                    disorder += 1
        return (disorder % 2 == 0)
