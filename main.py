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

    puzzle1 = Puzzle(puzzleSize)
    #puzzle2 = Puzzle(puzzleSize)

    #Puzzle.setBoard(puzzle2, [[1, 2, 3], [0, 4, 6], [7, 5, 8]])

    print(puzzle1)

    a = Astar(puzzle1, 0)
    node = a.solve()
    print("Output:")


main()
