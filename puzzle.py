class Puzzle:

    def __init__(self, board, size, h, g):
        self.board = board  # matrix
        self.size = size  # size of puzzle (8,15,24)
        self.h = 0  # heuristic
        self.g = 0  # cost to reach goal

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

    def printPuzzle(size, board):
        """
        prints puzzle matrix with proper format
        """
        puzzle_len = size
        if puzzle_len == 8:
            for row in board:
                print("{: >5} {: >5} {: >5}".format(*row))
        elif puzzle_len == 15:
            for row in board:
                print("{: >5} {: >5} {: >5} {: > 5}".format(*row))

        else:  # if puzzle size is 24 (5)
            for row in board:
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
