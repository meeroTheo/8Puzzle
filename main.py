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

    result_steps3=[]
    result_nodecount3=[]
    result_steps2=[]
    result_nodecount2=[]
    result_steps1=[]
    result_nodecount1=[]
    for x in range(25):
        print("{}%".format(int(x/25)*100))
        timeOut=False
        puzzle = Puzzle(puzzleSize)
        a = Astar(puzzle, 0)
        steps, nc, timeOut = a.solve1()
        if (not timeOut):
            result_steps1.append(steps)
            result_nodecount1.append(nc)
            print("done h1")
        else:
            print("timeout")
            x-=1
            continue
        print("---------------------")
        print(puzzle)
        print("---------------------")
        steps, nc= a.solve2()
        result_steps2.append(steps)
        result_nodecount2.append(nc)
        steps, nc = a.solve3()
        result_steps3.append(steps)
        result_nodecount3.append(nc)
    
    print(result_steps1)
    print(result_nodecount1)
    print(result_steps2)
    print(result_nodecount2)
    print(result_steps3)
    print(result_nodecount3)

main()
