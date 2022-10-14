
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
        self.puzzle.f1 = self.heuristic1() + self.puzzle.g
        return

    def f2(self):
        self.puzzle.f2 = self.heuristic2() + self.puzzle.g
        return

    def f3(self):
        self.puzzle.f3 = self.heuristic3() + self.puzzle.g
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
        Returns the new state
        """
        # check if the move is valid
        if (not ((x2 < self.puzzle.size and x2 >= 0)
                 and (y2 < self.puzzle.size and y2 >= 0))):
            return None

        # swap the 0 with the adjacent node
        tempState = self.deepcopy()
        tempVal = tempState.board[x2][y2]
        tempState.board[x2][y2] = tempState.board[x1][y1]

        tempState.board[x1][y1] = tempVal
        tempState.g += 1
        return tempState

    def deepcopy(self):

        temp = Puzzle(((self.puzzle.size) ** 2)-1, self.puzzle.g,
                      self.puzzle.f1, self.puzzle.f2, self.puzzle.f3)

        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                temp.board[i][j] = self.puzzle.board[i][j]

        return temp

    def solve(self):
        """
        Solve the 8 puzzle using A* Search
        """
        start = Puzzle(self.puzzle.size, 0, 0, 0, 0)
        startNode = Astar(start)

        visit1 = deque()
        visit2 = deque()
        visit3 = deque()

        # flag to indicate solved puzzle
        flag1 = False
        flag2 = False
        flag3 = False

        # put in while loop
        while not (flag1 and flag2 and flag3):
            x, y = self.findzero()
            coords = [[x, y-1], [x, y+1], [x-1, y],
                      [x+1, y]]  # up down left right

            for i in coords:
                # get the state of the adjacent node
                path = self.moves(x, y, i[0], i[1])
                print(x, y)

                if path:
                    # create a new node with the state of the adjacent node
                    pathz = Astar(path)
                    # calculate heuristic function(comment)
                    if not (flag1):
                        pathz.f1()
                        visit1.appendleft(pathz)
                    if not (flag2):
                        pathz.f2()
                        visit2.appendleft(pathz)
                    if not (flag3):
                        pathz.f3()
                        visit3.appendleft(pathz)
            # sort to find the node with the lowest f value which represents the best path
            if not (flag1):
                visit1 = deque(
                    sorted(list(visit1), key=lambda x: self.puzzle.f1))
                node1 = visit1.popleft()
            if not (flag2):
                visit2 = deque(
                    sorted(list(visit2), key=lambda x: self.puzzle.f2))
                node2 = visit2.popleft()
            if not (flag3):
                visit3 = deque(
                    sorted(list(visit3), key=lambda x: self.puzzle.f3))
                node3 = visit3.popleft()

            self.puzzle = node1.puzzle
            Puzzle.printPuzzle(node1.puzzle)

            break
            if node1.heuristic1() == 0:
                print("node1 found")
                flag1 = True
                break

            if node2.heuristic2() == 0:
                print("node2 found")
                flag2 = True
                break

            if node3.heuristic3() == 0:
                print("node 3 found")
                flag3 = True
                break

        return node1
