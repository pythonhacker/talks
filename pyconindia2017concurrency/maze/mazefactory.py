"""

Provides different ways (factory methods) to build Mazes

"""

import random
import json
from maze import Maze

class MazeReaderException(Exception):
    pass

class MazeReader(object):
    """ Read a maze from different input sources """

    STDIN = 0
    FILE = 1
    SOCKET = 2

    def __init__(self):
        self.maze_rows = []
        pass

    def readStdin(self):
        """ Read a maze from standard input """

        print('Enter a maze')
        print('You can enter a maze row by row')
        print()
        
        data = input('Enter the dimension of the maze as Width X Height: ')
        w, h = data.split()
        w, h  = int(w), int(h)
        
        for x in range(h):
            row = ''
            while not row:
                row = input('Enter row number %d: ' % (x+1))
            row = row.split()
            if len(row) != w:
                raise MazeReaderException('invalid size of maze row')
            self.maze_rows.append(row)

    def readFile(self):
        """ Read a maze from an input file """

        fname = input('Enter maze filename: ')
        self.maze_rows = json.load(open(fname))

    def getData(self):
        return self.maze_rows

    def readMaze(self, source=STDIN):
        """ Read a maze from the input source """

        if source==MazeReader.STDIN:
            self.readStdin()
        elif source == MazeReader.FILE:
            self.readFile()

        return self.getData()

    
class MazeFactory(object):
    """ Factory class for Maze object """

    def makeMaze(self, source=MazeReader.STDIN):
        """ Create a maze and return it. The source is
        read from the 'source' argument """

        reader = MazeReader()
        return Maze(reader.readMaze(source))

    def makeRandomMaze(self, dimension):
        """ Generate a random maze of size dimension x dimension """

        rows = []
        for x in range(dimension):
            row = []
            for y in range(dimension):
                row.append(random.randrange(2))
            random.shuffle(row)
            rows.append(row)

        return Maze(rows)

        
