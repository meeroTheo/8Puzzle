
from queue import PriorityQueue
import re
from puzzle import Puzzle

from collections import deque


class Astar:

    def __init__(self, puzzle, g):
        self.puzzle = puzzle
        self.explored = False
        self.g = g
        self.f1 = self.puzzle.h1 + self.g
        self.f2 = self.puzzle.h2 + self.g
        self.f3 = self.set_f3()
        self.children = []

    def set_f1(self):
        """
        return estimated total cost
        of cheapest solution for h1
        """
        self.f1 = self.puzzle.h1 + self.g
        return

    def set_f2(self):
        self.f2 = self.puzzle.h2 + self.g
        return

    def set_f3(self):
        self.f3 = self.puzzle.h3 + self.g
        return

    def isVisited(self):
        return self.visited

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
        pqueue.append((parent.f1, parent))
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
                        Puzzle.printPuzzle(new_puzzle)
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
                        seen.append(new_puzzle)
                        child = Astar(new_puzzle, g)
                        pqueue.append((child.f1, child))
                        pqueue.sort(key=lambda x: x[0], reverse=True)
            Puzzle.printPuzzle(node.puzzle)
            print(node.f1)
            if (node.puzzle.h1 == 0):
                break

    '''
        g = 0
        parentnode = Astar(root, g)
        g += 1
        for i in coords:
            new_puzzle = parentnode.puzzle.moves(x,y,i[0],i[1])
            isVisited = False
            # checks if new_puzzle's state has been seen before, if seen before the old Astar object will be put into children
            for node in visited:
                if node.puzzle == new_puzzle:
                    isVisited = True
                    parentnode.children.append(node)
                    break
            # if state has never been seen before, create a new Astar object with the new state and put in children
            if not isVisited:
                child = Astar(new_puzzle, g)
                parentnode.children.append(child)
            #put parent node in visited and mark it as explored
            visited.append(parentnode)
            parentnode.explored = True

        if parentnode.children[0] is not None:
            optimal = parentnode.children.f1
        allExplored = False
        for j in parentnode.children:
            if j.explored == True:
                allExplored = True
        for k in parentnode.children:
            if not allExplored and k.explored == False and k.f1 < optimal:
                optimal = k.f1
                
            elif allExplored and k.f1 < optimal:
                optimal = k.f1
        '''
