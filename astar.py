
from puzzle import Puzzle
from math import sqrt
from collections import deque


class Astar:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def f1(puzzle):
        """
        return estimated total cost
        of cheapest solution for h1
        """
        puzzle.f1 = Astar.heuristic1(puzzle) + puzzle.g
        return

    def f2(puzzle):
        puzzle.f2 = Astar.heuristic2(puzzle) + puzzle.g
        return

    def f3(puzzle):
        puzzle.f3 = Astar.heuristic3(puzzle) + puzzle.g
        return

    def heuristic1(puzzle):
        """
        misplaced tiles
        """
        count = 0
        board = puzzle.board
        goalstate = puzzle.puzzleEndState()
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                if ((board[i][j] != goalstate[i][j]) and board[i][j] != 0):
                    count += 1

        return count

    def heuristic2(puzzle):
        """
        manhattan distance
        """
        distance = 0
        board = puzzle.board
        size = puzzle.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += abs(x-i)+abs(y-j)  # 0
        return distance

    def heuristic3(puzzle):
        distance = 0
        board = puzzle.board
        size = puzzle.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += sqrt((x-i)**2 + (y-j)**2)

    def findzero(puzzle):
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                if (puzzle.board[i][j] == 0):
                    return i, j

    def moves(puzzle, x1, y1, x2, y2):
        """
        Gets the state of an adjacent node
        which we swap with the 0
        Returns the new state
        """
        # check if the move is valid
        if (not ((x2 < puzzle.size and x2 >= 0)
                 and (y2 < puzzle.size and y2 >= 0))):
            return None

        # swap the 0 with the adjacent node
        tempState = Astar.deepcopy(puzzle)
        tempVal = tempState.board[x2][y2]
        tempState.board[x2][y2] = tempState.board[x1][y1]

        tempState.board[x1][y1] = tempVal
        tempState.g += 1
        return tempState

    def deepcopy(puzzle):

        temp = Puzzle(((puzzle.size) ** 2)-1, puzzle.g,
                      puzzle.f1, puzzle.f2, puzzle.f3)

        for i in range(puzzle.size):
            for j in range(puzzle.size):
                temp.board[i][j] = puzzle.board[i][j]

        return temp

    def solve(self):
        """
        Solve the 8 puzzle using A* Search
        """
        see = deque()
        seen = set()
        seen.add(self.puzzle)

        # put in while loop
        count = 0
        current = self.puzzle
        while True:
            count+=1
            x, y = Astar.findzero(current)
            coords = [[x, y-1], [x, y+1], [x-1, y],
                      [x+1, y]]  # up down left right
            print(x, y)
            for i in coords:
                # get the state of the adjacent node
                path = Astar.moves(current,x, y, i[0], i[1])
                if path:
                    # create a new node with the state of the adjacent node
                    
                    # calculate heuristic function
                    Astar.f1(path)
                    if (path not in seen):
                        see.appendleft(path)

            # sort to find the node with the lowest f value which represents the best path
            print(see)
            see = deque(
                    sorted(list(see), key=lambda path: path.f1))
            node1 = see.popleft()

            seen.add(node1)
            current=node1
            node1.print() #testing
            see.clear()
            print("-------------------------------")
            if(count == 5):
                break

        
        return node1
