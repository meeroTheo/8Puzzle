
from queue import PriorityQueue
from puzzle import Puzzle
import time
from collections import deque


class Astar:

    def __init__(self, puzzle, g):
        self.puzzle = puzzle
        self.explored = False
        self.parent = None
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

    def set_f2(self):
        self.f2 = self.puzzle.h2 + self.g
        return
    def set_f1(self):
        self.f1 = self.puzzle.h1 + self.g
        return

    def set_f3(self):
        self.f3 = self.puzzle.h3 + self.g
        return

    def findzero(self, puzzle):
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                if (puzzle.board[i][j] == 0):
                    return i, j

    def solve1(self):
        start_time=time.time()
        pqueue = []
        seen = set()
        nodecount = 0
        g = 0
        pqueue.append((self.f1, self))
        seen.add(str(self.puzzle))
        count = 0
        while True:
            # evaluates node in priority queue with smallest f case
            node = pqueue.pop()[1]
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h3()
                    if new_puzzle.h3 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    if (str(new_puzzle) not in seen):
                        nodecount+=1
                        seen.add(str(new_puzzle))
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f1
                        pqueue.append((child.f1, child))  # add to queue
                        # sort queue
                        pqueue.sort(key=lambda x: x[0], reverse=True)
            # print(node.puzzle)
            #print(node.g)
            count += 1
            # if (count == 100):
            #    break
            if (node.puzzle.h3 == 0):
                route = []
                #print("\n")
                #print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                #route.reverse()
                #print("Number of steps: ")
                #print(steps)
                #for state in route:
                    #print(state.puzzle)
                break
            if((time.time()-start_time) > 30):
                return g,nodecount,True
        return steps, nodecount, False

    def solve2(self):
        pqueue = []
        seen = set()
        nodecount = 0
        g = 0
        pqueue.append((self.f2, self))
        seen.add(str(self.puzzle))
        count = 0
        while True:
            # evaluates node in priority queue with smallest f case
            node = pqueue.pop()[1]
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h1()
                    if new_puzzle.h1 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    if (str(new_puzzle) not in seen):
                        nodecount+=1
                        seen.add(str(new_puzzle))
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f2
                        pqueue.append((child.f2, child))  # add to queue
                        # sort queue
                        pqueue.sort(key=lambda x: x[0], reverse=True)
            # print(node.puzzle)
            #print(node.g)
            count += 1
            # if (count == 100):
            #    break
            if (node.puzzle.h3 == 0):
                route = []
                #print("\n")
                #print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                #route.reverse()
                #print("Number of steps: ")
                #print(steps)
                #for state in route:
                    #print(state.puzzle)
                break
        return steps, nodecount

    def solve3(self):
        pqueue = []
        seen = set()
        nodecount= 0
        g = 0
        pqueue.append((self.f3, self))
        seen.add(str(self.puzzle))
        count = 0
        while True:
            # evaluates node in priority queue with smallest f case
            node = pqueue.pop()[1]
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h3()
                    if new_puzzle.h3 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    if (str(new_puzzle) not in seen):
                        nodecount+=1
                        seen.add(str(new_puzzle))
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f3
                        pqueue.append((child.f3, child))  # add to queue
                        # sort queue
                        pqueue.sort(key=lambda x: x[0], reverse=True)
            # print(node.puzzle)
            #print(node.g)
            count += 1
            # if (count == 100):
            #    break
            
            if (node.puzzle.h3 == 0):
                route = []
                #print("\n")
                #print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                #route.reverse()
                #print("Number of steps: ")
                #print(steps)
                #for state in route:
                    #print(state.puzzle)
                break
        return steps, nodecount
