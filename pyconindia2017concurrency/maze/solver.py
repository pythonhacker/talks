"""

Maze solver using Backtracking

"""

import random
import copy
import os

from colors import *
from multiprocessing import Process

class MazeSolver(object):
    """ Maze solver class """
    
    def __init__(self, maze, silent=False):
        self.maze = maze
        self._start = (0,0)
        self._end = (0,0)
        # Current point
        self._current = (0,0)
        # Solve path
        self._path = []
        # Number of cyclic loops
        self._loops = 0
        # Solvable flag
        self.unsolvable = False        
        # xdiff
        self._xdiff = 0.0
        # ydiff
        self._ydiff = 0.0
        # List keeping cycles (generations)
        self.cycles = []
        # Number of retraces
        self._numretrace = 0
        # Map for exit points
        self._pointmap = {}
        # Number of all zero points
        self._numzeropts = 0
        # Map for retraced points
        self._retracemap = {}
        # Cache for keys of above
        self._retracekeycache = []
        # Number of times retracemap is not updated
        # with a new point
        self._lastupdate = 0
        # Abort flag
        self.abort = False
        # Shared state
        self.state = None
        # Silent ?
        self.silent = silent

    def setStartPoint(self, pt):

        self.maze.validatePoint(pt)
        self._start = pt

    def setEndPoint(self, pt):

        self.maze.validatePoint(pt)
        self._end = pt

    def boundaryCheck(self):
        """ Check boundaries of start and end points """

        exits1 = self.getExitPoints(self._start)
        exits2 = self.getExitPoints(self._end)        

        if len(exits1)==0 or len(exits2)==0:
            return False

        return True

    def setCurrentPoint(self, point):
        """ Set the current point """

        # print 'Current point is',point
        self._current = point
        self._xdiff = abs(self._current[0] - self._end[0])
        self._ydiff = abs(self._current[1] - self._end[1])
        
        self._path.append(point)

    def isSolved(self):
        """ Whether the maze is solved """

        return (self._current == self._end)

    def isFinished(self):
        """ Whether maze is solved or deadlocked """

        return self.isSolved() or self.unsolvable
    
    def checkDeadLock(self, point1, point2):

        pt1 = self.getClosestPoint(self.getExitPoints(point1))
        pt2 = self.getClosestPoint(self.getExitPoints(point2))

        if pt1==point2 and pt2==point1:
            return True

        return False

    def getExitPoints(self, point):
        """ Get exit points for 'point' """

        points = self._pointmap.get(point)

        if points==None:
            # We are using shortest-distance algorithm
            points = self.maze.getExitPoints(point)
            self._pointmap[point] = points

        return points
        
    def getNextPoint(self):
        """ Get the next point from the current point """

        # Get all exit points from current point
        points = self.getExitPoints(self._current)
        point = self.getBestPoint(points)
        
        while self.checkClosedLoop(point):

            if self.endlessLoop():
                point = None
                break
            
            # Save point
            point2 = point

            point = self.getNextClosestPointNotInPath(points, point2)
            if not point:
                # Try back tracking to find a new path
                point = self.backTrack()
                
        return point

    def backTrack(self):
        """ Backtrack to find a new solution """
        
        # Backtrack point by point in path, till
        # you get to a point which provides an
        # alternative.
        
        print('Backtracking...')
        path = self._path[:]
        path.reverse()

        self._numretrace += 1
        
        try:
            idx = path[1:].index(self._current)
        except:
            idx = path.index(self._current)            

        pathstack = []
        
        for x in range(idx+1, len(path)):
            p = path[x]
            if p in pathstack: continue

            pathstack.append(p)
            if p != self._path[-1]:
                # print 'Current point is',p
                self._path.append(p)

            if p != self._start:
                points = self.getExitPoints(p)
                point = self.getNextClosestPointNotInPath(points, self.getClosestPoint(points))
                self._retracemap[p] = self._retracemap.get(p, 0) + 1
            else:
                # Add path to cycle
                path = self.sortPointsByXYDistance(self._path[:-1])
                self.cycles.append((path, self._path[:-1]))
                # Reset solver state
                self._path = []
                self._loops = 0
                self._retracemap[p] = self._retracemap.get(p, 0) + 1
                
                return p

    def endlessLoop(self):

        if self._retracemap:
            # If the retrace map has not been updated for a while
            # increment lastupdate count
            if self._retracemap.keys() == self._retracekeycache:
                self._lastupdate += 1
            self._retracekeycache = self._retracemap.keys()

        # If lastupdate count reaches the total number of points
        # it could mean we exhausted all possible paths.
        if self._lastupdate > self.maze.getWidth()*self.maze.getHeight():
            print('Exited because of retracekeycache overflow')
            return True

        # If retrace has gone through all zero points and not
        # yet found a solution, then we are hitting a dead-lock.
        elif len(self._retracemap.keys())> self._numzeropts - 1:
            print('Exited because number of points exceeded zero points')
            return True
        else:
            # If the retrace path contains only one point
            if len(self._retracemap.keys())==1:
                val = self._retracemap.get(list(self._retracemap.keys())[0])
                # If we hit the same point more than the number of
                # zero points in the maze, it signals a dead-lock.
                if val>self._numzeropts:
                    print('Exited because we are oscillating')
                    return True
        
        return False
        
    def checkClosedLoop(self, point):
        """ See if this point is causing a closed loop """

        l = range(0, len(self._path)-1, 2)

        for x in reversed(l):
            if self._path[x] == point:
                self._loops += 1
                # loop = tuple(self._path[x:])
                # print 'Point=>',point, len(self._path)
                return True

        return False
    
    def getBestPoint(self, points):
        """ Get the best point """

        # Not yet formed any cycles
        if len(self.cycles)==0:
            # First try min point
            point = self.getClosestPoint(points)
            # Save point
            point2 = point
            # Point for trying alternate
            altpoint = point

            point = self.getNextClosestPointNotInPath(points, point2)
            if not point:
                point = point2
        else:
            allcycles=[]
            # map(allcycles.extend, [item[0] for item in self.cycles])
            [allcycles.extend(x) for x in [item[0] for item in self.cycles]]
            
            #for item in self.cycles:
            #    allcycles.append(item[0])
            
            if self._current==self._start or self._current in allcycles:
                # print 'FOUND IT =>',self._current
                history = []
                for path in [item[1] for item in self.cycles]:
                    path.reverse()
                    try:
                        idx = path.index(self._current)
                        next = path[idx-1]
                        history.append(next)
                    except:
                        pass

                point = self.getDifferentPoint(points, history)
                if not point:
                    point = self.getAlternatePoint(points, history[-1])
            else:
                # Not there 
                point2 = self.getClosestPoint(points)
                point = self.getNextClosestPointNotInPath(points, point2)
                if not point:
                    point = point2
                
            altpoint = point
            
        return point

    def sortPointsByXYDistance(self, points):
        """ Sort list of points by X+Y distance """

        distances = [(self.maze.calcXYDistance(point, self._end), point) for point in points]
        distances.sort()
            
        points2 = [item[1] for item in distances]

        return points2
    
    def sortPointsByDistances(self, points):
        """ Sort points according to distance from end point """

        if self._xdiff>self._ydiff:
            distances = [(self.maze.calcXDistance(point, self._end), point) for point in points]
        elif self._xdiff<self._ydiff:
            distances = [(self.maze.calcYDistance(point, self._end), point) for point in points]
        else:
            distances = [(self.maze.calcXYDistance(point, self._end), point) for point in points]

        distances.sort()
        points2 = [item[1] for item in distances]

        return points2

    def sortPoints(self, points):

        return self.sortPointsByDistances(points)
        
    def getClosestPoint(self, points):
        """ Return the closest point from current
        to the end point from a list of exit points """

        points2 = self.sortPoints(points)
        
        # Min distance point
        closest = points2[0]
        return closest

    def getDifferentPoint(self, points1, points2):
        """ Return a random point in points1 which is not
        in points2 """

        l = [pt for pt in points1 if pt not in points2]
        if l:
            return random.choice(l)

        return None
        
    def getAlternatePoint(self, points, point):
        """ Get alternate point """

        print('Trying alternate...',self._current, point, points)
        points2 = points[:]

        if point in points2:
            points2.remove(point)
        if points2:
            return random.choice(points2)
        else:
            return point
        
        return None

    def getNextClosestPoint(self, points, point):
        """ After point 'point' get the next closest point
        to the end point from list of points """

        points2 = self.sortPoints(points)
        idx = points2.index(point)

        try:
            return points2[idx+1]
        except:
            return None

    def getNextClosestPointNotInPath(self, points, point):

        point2 = point
        while point2 in self._path:
            point2 = self.getNextClosestPoint(points, point2)
            
        return point2

    def preSolve(self):
        """ Steps before solving """

        print('Starting point is', self._start)
        print('Ending point is', self._end)
        
        # First check if both start and end are same
        if self._start == self._end:
            print('Start/end points are the same. Trivial maze.')
            print [self._start, self._end]
            return False
        
        # Check boundary conditions
        if not self.boundaryCheck():
            print('Either start/end point are unreachable. Maze cannot be solved.')
            return False

        # Proper maze
        print('Maze is a proper maze.')

        # Initialize solver
        self.setCurrentPoint(self._start)
        self._numzeropts = len(self.maze.getAllZeroPoints())
        
        self.unsolvable = False

        return True
    
    def postSolve(self):
        """ Steps after solving """

        if self.state != None:
            print('Solver %s' % os.getpid(), 'solved the maze. Printing result ...')
                
        self.printResult()
        if not self.unsolvable:
            print('Final solution path is',self._path)
            print('Length of path is',len(self._path))
        else:
            print('Path till deadlock is',self._path)
            print('Length of path is',len(self._path))      

    def length(self):
        """ Return length of the solution path """

        return len(self._path)
        
    def doSolve(self):
        """ Actual solution step """

        while not (self.isSolved() or self.abort):
            if self.state != None and self.state.value == 1:
                print('Solver %s' % os.getpid(), '=> Maze got solved already')
                self.abort = True
                break
            
            pt = self.getNextPoint()
            
            if pt:
                self.setCurrentPoint(pt)
            else:
                print('Dead-lock - maze unsolvable')
                self.unsolvable = True
                break

        if not self.abort:
            if self.state != None:
                self.state.value = 1
            
    def solve(self, state=None):
        """ Solve the maze """

        if not self.preSolve():
            return

        self.state = state
        if self.state != None:
            print('Solver %s' % os.getpid(), 'starting...')
        else:
            print('Solving...')
            
        self.doSolve()

        if self.abort:
            return
        
        self.postSolve()

        return {'path': self._path, 'solved': not self.unsolvable, 'id': os.getpid()}

    def printResult(self):
        """ Print the maze
		 showing the path """
        
        if self.silent:
            return False
        
        for x,y in self._path:
            if self.unsolvable:
                self.maze.setItem(x,y, '*')
            else:
                self.maze.setItem(x,y, '+')

        self.maze.setItem(self._start[0], self._start[1], 'S')
        self.maze.setItem(self._end[0], self._end[1], 'F')        

        if self.unsolvable:
            print('Maze with final path')
        else:
            print('Maze with solution path')
            
        print(self.maze)

        
