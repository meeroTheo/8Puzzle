
from puzzle import Puzzle
from math import sqrt
from collections import deque


class Astar:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def f1(self):
        """
        return estimated total cost 
        of cheapest solution for h1
        """
        self.puzzle.f1 = self.heuristic1 + self.puzzle.g
        return

    def f2(self):
        self.puzzle.f2 = self.heuristic2 + self.puzzle.g
        return

    def f3(self):
        self.puzzle.f3 = self.heuristic3 + self.puzzle.g
        return

    def heuristic1(self):
        """
        misplaced tiles
        """
        count = 0
        board = self.puzzle.board
        goalstate = self.puzzle.puzzleEndState()
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
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += abs(x-i)+abs(y-j)  # 0
        return distance

    def heuristic3(self):
        distance = 0
        board = self.puzzle.board
        size = self.puzzle.size
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    x = (board[i][j]-1)//size  #
                    y = (board[i][j]-1) % size  #
                    distance += sqrt((x-i)**2 + (y-j)**2)

        return distance

    def findzero(self):
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                if (self.puzzle.board[i][j] == 0):
                    return i, j

    def moves(self, x1, y1, x2, y2):
        """
        Gets the state of an adjacent node 
        which we swap with the 0
        """
        # check if out of bounds
        if (not ((x2 < self.puzzle.size and x2 >= 0)
                 and (y2 < self.puzzle.size and y2 >= 0))):
            return None

        # swap
        tempState = self.deepcopy(self.puzzle)
        tempVal = tempState.board[x2][y2]
        tempState.board[x2][y2] = tempState.board[x1][y1]

        tempState.board[x1][y1] = tempVal
        tempState.g += 1
        return tempState

    def solve(self):

        initialState = self.puzzle.board
        goalState = self.puzzle.puzzleEndState()
        start = Puzzle(initialState, self.puzzle.size, 0, 0, 0, 0)
        goal = Puzzle(goalState, self.puzzle.size, 0, 0, 0, 0)

        startNode = Astar(start)
        endNode = Astar(goal)
        g = self.puzzle.g

        x, y = self.findzero()
        coords = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]

        visit1 = deque(startNode)
        visit2 = deque(startNode)
        visit3 = deque(startNode)

        for i in coords:

            path = self.moves(x, y, i[0], i[1])
            if path:
                pathz = Astar(path)
                # calculate heuristic function(comment)
                pathz.f1()
                pathz.f2()
                pathz.f3()
                visit1.add(pathz)
                visit2.add(pathz)
                visit3.add(pathz)

        visit1 = deque(sorted(list(visit1), key=lambda puzzle: puzzle.f1))
        visit2 = deque(sorted(list(visit2), key=lambda puzzle: puzzle.f2))
        visit3 = deque(sorted(list(visit3), key=lambda puzzle: puzzle.f3))

        return
