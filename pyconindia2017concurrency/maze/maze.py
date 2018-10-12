#-*-*-coding: utf-8

## {{{ http://code.activestate.com/recipes/496884/ (r10)
"""
Amaze - A completely object-oriented Pythonic maze generator/solver.
This can generate random mazes and solve them. It should be
able to solve any kind of maze and inform you in case a maze is
unsolveable.

This uses a very simple representation of a mze. A maze is
represented as an mxn matrix with each point value being either
0 or 1. Points with value 0 represent paths and those with
value 1 represent blocks. The problem is to find a path from
point A to point B in the matrix.

The matrix is represented internally as a list of lists.

Have fun :-)

"""

import sys
import random
import json
from colors import *

class MazeError(Exception):
    """ An exception class for Maze """
    
    pass

class Maze(object):
    """ A class representing a maze """

    def __init__(self, rows=[[]]):
        self._rows = rows
        self.__validate()
        self.__normalize()

    def __str__(self):

        s = '\n'
        for row in self._rows:
            for item in row:
                if item == 0:
                    line = ''.join((G + ' ' + W, G + ' ' + W, G + ' ' + W))
                elif item == 1:
                    line = ''.join((R + ' ' + W, R + ' ' + W, R + ' ' + W))
                elif item == '*':
                    line = ''.join((O + ' ' + W, O + '*' + W, O + ' ' + W))
                elif item == '+':
                    line = ''.join((B + ' ' + W, B + '+' + W, B + ' ' + W))
                else:
                    line = ''.join((W + ' ' + W, W + str(item) + W, W + ' ' + W))
                    
                s = ''.join((s, line))
                
            s = ''.join((s,'\n'))
            # s += '-'*len(s) + '\n'

        return s

    def save(self):
        json.dump(self._rows, open('maze.json','w'))
                     
    def __validate(self):
        """ Validate the maze """

        # Get length of first row
        width = len(self._rows[0])
        widths = [len(row) for row in self._rows]
        if widths.count(width) != len(widths):
            raise MazeError('Invalid maze!')

        self._height = len(self._rows)
        self._width = width

    def __normalize(self):
        """ Normalize the maze """

        # This converts any number > 0 in the maze to 1
        for x in range(len(self._rows)):
            row = self._rows[x]
            row = list(map(lambda x: min(int(x), 1), row))
            self._rows[x] = row

    def getHeight(self):
        """ Return the height of the maze """

        return self._height

    def getWidth(self):
        """ Return the width of the maze """

        return self._width

    def validatePoint(self, pt):
        """ Validate the point pt """

        x,y = pt
        w = self._width
        h = self._height
        
        # Don't support Pythonic negative indices
        if x > w - 1 or x<0:
            raise MazeError('x co-ordinate out of range!')

        if y > h - 1 or y<0:
            raise MazeError('y co-ordinate out of range!')

        pass
    
    def getItem(self, x, y):
        """ Return the item at location (x,y) """

        self.validatePoint((x,y))
        
        w = self._width
        h = self._height

        # This is based on origin at bottom-left corner
        # y-axis is reversed w.r.t row arrangement
        # Get row
        row = self._rows[h-y-1]
        return row[x]

    def setItem(self, x, y, value):
        """ Set the value at point (x,y) to 'value' """

        h = self._height
        
        self.validatePoint((x,y))
        row = self._rows[h-y-1]
        row[x] = value
        

    def getNeighBours(self, pt):
        """ Return a list of (x,y) locations of the neighbours
        of point pt """

        self.validatePoint(pt)

        x,y = pt
        
        h = self._height
        w = self._width
        
        # There are eight neighbours for any point
        # inside the maze. However, this becomes 3 at
        # the corners and 5 at the edges
        poss_nbors = (x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1)

        nbors = []
        for xx,yy in poss_nbors:
            if (xx>=0 and xx<=w-1) and (yy>=0 and yy<=h-1):
                nbors.append((xx,yy))

        return nbors
        
    def getExitPoints(self, pt):
        """ Return a list of exit points at point pt """

        # Get neighbour list and return if the point value
        # is 0

        exits = []
        for xx,yy in self.getNeighBours(pt):
            if self.getItem(xx,yy)==0:
                exits.append((xx,yy))

        return exits

    def getRandomExitPoint(self, pt):
        """ Return a random exit point at point (x,y) """

        return random.choice(self.getExitPoints(pt))

    def getRandomStartPoint(self):
        """ Return a random point as starting point """

        return random.choice(self.getAllZeroPoints())

    def getRandomEndPoint(self):
        """ Return a random point as ending point """

        return random.choice(self.getAllZeroPoints())

    def getAllZeroPoints(self):
        """ Return a list of all points with
        zero value """
        
        points = []
        for x in range(self._width):
            for y in range(self._height):
                if self.getItem(x,y)==0:
                    points.append((x,y))

        return points
        
    def calcDistance(self, pt1, pt2):
        """ Calculate the distance between two points """

        # The points should be given as (x,y) tuples
        self.validatePoint(pt1)
        self.validatePoint(pt2)        
        
        x1,y1 = pt1
        x2,y2 = pt2

        return pow( (pow((x1-x2), 2) + pow((y1-y2),2)), 0.5)

    def calcXDistance(self, pt1, pt2):
        """ Calculate the X distance between two points """

        # The points should be given as (x,y) tuples
        self.validatePoint(pt1)
        self.validatePoint(pt2)
        
        x1, y1 = pt1
        x2, y2 = pt2

        return abs(x1-x2)

    def calcYDistance(self, pt1, pt2):
        """ Calculate the Y distance between two points """

        # The points should be given as (x,y) tuples
        self.validatePoint(pt1)
        self.validatePoint(pt2)
        
        x1, y1 = pt1
        x2, y2 = pt2

        return abs(y1-y2)

    def calcXYDistance(self, pt1, pt2):
        """ Calculate the X-Y distance between two points """

        # The points should be given as (x,y) tuples
        self.validatePoint(pt1)
        self.validatePoint(pt2)
        
        x1, y1 = pt1
        x2, y2 = pt2

        return abs(y1-y2) + abs(x1-x2)
        
    def getData(self):
        """ Return the maze data """

        return self._rows


    
## end of http://code.activestate.com/recipes/496884/ }}}
