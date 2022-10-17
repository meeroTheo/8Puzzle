
from queue import PriorityQueue
from puzzle import Puzzle

from collections import deque


class Astar:

    def __init__(self, puzzle, g):
        self.puzzle = puzzle
        self.explored = False
        self.g = g
        self.f1 = self.puzzle.h1 + self.g
        self.f2 = self.puzzle.h2 + self.g
        self.f3 = self.puzzle.h3 + self.g
        self.children = []

    def set_f(self):
        """
        return estimated total cost
        of cheapest solution for h1
        """
        self.f1 = self.puzzle.h1 + self.g
        self.f2 = self.puzzle.h2 + self.g
        self.f3 = self.puzzle.h3 + self.g
        return



    def findzero(self, puzzle):
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                if (puzzle.board[i][j] == 0):
                    return i, j

    def solve(self):
        seen = []
        pqueue = []
        g = 0
        goalstate = Puzzle(self.puzzle.size)
        Puzzle.setBoard(goalstate, Puzzle.puzzleEndState(goalstate))
        parent = self
        seen.append(parent.puzzle)
        pqueue.append((parent.f2, parent))
        while True:
            # evaluates node in priority queue with smallest f case
            node = pqueue.pop()[1]
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle is not None:
                    Puzzle.setBoard(new_puzzle, new_puzzle.board)
                    if Puzzle.isEqual(new_puzzle, goalstate):
                        print(new_puzzle)
                        return new_puzzle
                    isSeen = False
                    j = 0
                    # checks if path has been seen before
                    while j < len(seen):
                        if Puzzle.isEqual(new_puzzle, seen[j]):
                            isSeen = True
                            break
                        j += 1
                    # puts unseen states into priority queue
                    if not isSeen:
                        seen.append(new_puzzle)  # add to seen
                        child = Astar(new_puzzle, g)  # create child
                        pqueue.append((child.f2, child))  # add to queue
                        # sort queue
                        pqueue.sort(key=lambda x: x[0], reverse=True)
            print(node.puzzle)
            print(node.f2)
            if (node.puzzle.h1 == 0):
                break
        return node.puzzle
