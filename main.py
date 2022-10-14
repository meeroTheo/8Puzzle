from puzzle import Puzzle
from astar import Astar


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

    puzzle1 = Puzzle(puzzleSize, 0, 0, 0, 0)

    Puzzle.printPuzzle(puzzle1)

    a = Astar(puzzle1)

    node = a.solve()

    Puzzle.printPuzzle(node.puzzle)


main()
