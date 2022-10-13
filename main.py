
def main():
    """
    Main function

    """
    # Determines usable puzzle size by user input
    puzzleSize = 0
    puzzleSizeList = [8, 15, 24]
    while puzzleSize not in puzzleSizeList:
        puzzleSize = int(
            input("Enter puzzle size (8-puzzle, 15 puzzle, 24 puzzle): "))


def disorder(puzzle):
    """
    Determines the disorder parameter
    """
    size = len(puzzle)-1
    disorder_num = 0

    for i in range(size):
        for j in range(1+i, size):
            if (puzzle[j][i] > 0) and puzzle[j][i] > puzzle[i][j]:
                disorder += 1
    return disorder


def isSolvable(puzzle):
    """
    Determines if the puzzle is solvable (DP even)
    """
    disorder = disorder(puzzle)
    return (disorder % 2 == 0)
