class Puzzle:

    def __init__(self, board, size):
        self.board = board
        self.size = size

    def puzzleEndState(puzzle_size):
        if puzzle_size == 8:
            puzzleEndState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif puzzle_size == 15:
            puzzleEndState = [[1, 2, 3, 4], [5, 6, 7, 8],
                              [9, 10, 11, 12], [13, 14, 15, 0]]
        else:  # 24 puzzle
            puzzleEndState = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
                11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        return puzzleEndState
