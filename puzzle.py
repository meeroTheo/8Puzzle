class Puzzle:

    def __init__(self, board, size, h, g):
        self.board = board
        self.size = size
        self.h = 0
        self.g = 0

    def puzzleEndState(puzzle_size):
        """
        Predetermined goal state for puzzles

        """
        if puzzle_size == 8:
            puzzleEndState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif puzzle_size == 15:
            puzzleEndState = [[1, 2, 3, 4], [5, 6, 7, 8],
                              [9, 10, 11, 12], [13, 14, 15, 0]]
        else:  # 24 puzzle
            puzzleEndState = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
                11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        return puzzleEndState

    def printPuzzle(self, size, board):
        # prints puzzle matrix with proper format
        puzzle_len = self.size
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
