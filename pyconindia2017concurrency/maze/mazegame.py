"""

Different types of Maze game classes

"""

from mazefactory import MazeFactory, MazeReader
from solver import MazeSolver
from maze import Maze
import copy
import multiprocessing

# input = input

def solve(solver):
    return solver.solve()

class MazeGame(object):

    def __init__(self, w=0, h=0):
        self._start = (0,0)
        self._end = (0,0)
        
    def createMaze(self):
        return None

    def getStartEndPoints(self, maze):
        return None

    def runGame(self, concurrent=False, best=False):

        maze = self.createMaze()
        if not maze:
            return None
        
        self.getStartEndPoints(maze)
        maze.save()
        
        # maze.setItem(self._start[0], self._start[1], 'S')
        # maze.setItem(self._end[0], self._end[1], 'F')
        
        print(maze)
        
        # Dump it to maze.txt
        # open('maze.txt','w').write(str(maze))
        open ('maze_pts.txt','w').write(str(self._start) + ' ' + str(self._end) + '\n')

        if concurrent:
            procs, solvers = [], []
            if not best:
                # Pick the solver which finishes first
                state = multiprocessing.Value('i', 0)
            
                for i in range(8):
                    solver = MazeSolver(Maze(rows=maze._rows[:]), silent=False)
                    solver.setStartPoint(self._start)
                    solver.setEndPoint(self._end)
                    solvers.append(solver)
                
                    proc = multiprocessing.Process(target=solver.solve, args=(state,))
                    procs.append(proc)

                for proc in procs:
                    proc.start()
                
                for proc in procs:
                    proc.join()
                
            else:
                # Pick the best solver
                pool = multiprocessing.Pool(8)

                for i in range(8):
                    solver = MazeSolver(Maze(rows=maze._rows[:]), silent=True)
                    solver.setStartPoint(self._start)
                    solver.setEndPoint(self._end)
                    solvers.append(solver)

                results = pool.map(solve, solvers)
                # Pick the one which solved it
                solved_results = list(filter(lambda x: x['solved'], results))
                # Manufacture a solver - for printing results
                solvor = MazeSolver(maze)
                solvor.setStartPoint(self._start)
                solvor.setEndPoint(self._end)
                    
                if len(solved_results):
                    pick = sorted(solved_results, key=lambda x: len(x['path']))[0]
                    solvor._path = pick['path']
                    # Pick one with least length
                    print('Got',len(solved_results),'solutions with path lengths =>',list(map(lambda x: len(x['path']), solved_results)))
                    print('Process',pick['id'],'had the best solution at path length',len(pick['path']))
                else:
                    pick = sorted(results, key=lambda x: len(x['path']))[0]
                    solvor._path = pick['path']
                    solvor.unsolvable = True
                                        
                    print('No solved results.')
                    print('Process',pick['id'],'had the smallest solution at path length',len(pick['path']))

                solvor.printResult()
                
        else:
            solver = MazeSolver(maze)
            solver.setStartPoint(self._start)
            solver.setEndPoint(self._end)
            solver.solve()

class InteractiveMazeGame(MazeGame):

    def createMaze(self):
        f = MazeFactory()
        return f.makeMaze()

    def getStartEndPoints(self, maze):

        while True:
            try:
                pt1 = input('Enter starting point: ')
                x,y = pt1.split()
                self._start = (int(x), int(y))
                maze.validatePoint(self._start)
                break
            except:
                pass

        while True:
            try:
                pt2 = input('Enter ending point: ')
                x,y = pt2.split()
                self._end = (int(x), int(y))        
                maze.validatePoint(self._end)
                break
            except:
                pass        
        
class FilebasedMazeGame(MazeGame):

    def createMaze(self):
        f = MazeFactory()
        return f.makeMaze(MazeReader.FILE)

    def getStartEndPoints(self, maze):

        filename = input('Enter points file: ').strip()
        try:
            line = open(filename).readlines()[0].strip()
            l = line.split(')')
            self._start = eval(l[0].strip() + ')')
            self._end = eval(l[1].strip() + ')')
        except (OSError, IOError, Exception) as e:
            print(e)
            sys.exit(0)
        
class RandomMazeGame(MazeGame):

    def __init__(self, w=0, h=0):
        super(RandomMazeGame, self).__init__(w, h)
        self._dimension = w
        
    def createMaze(self):
        f = MazeFactory()
        return f.makeRandomMaze(self._dimension)    

    def getStartEndPoints(self, maze):

        pt1, pt2 = (0,0), (0,0)
        while pt1 == pt2:
            pt1 = maze.getRandomStartPoint()
            pt2 = maze.getRandomEndPoint()

        self._start = pt1
        self._end = pt2

class RandomMazeGame2(RandomMazeGame):
    """ Random maze game with distant points """

    def getStartEndPoints(self, maze):

        pt1, pt2 = (0,0), (0,0)
        flag = True
        while flag:
            pt1 = maze.getRandomStartPoint()
            pt2 = maze.getRandomEndPoint()
            # Try till points are at least
            # half maze apart
            xdist = maze.calcXDistance(pt1, pt2)
            ydist = maze.calcYDistance(pt1, pt2)            
            if xdist>=float(maze.getWidth())/2.0 or \
               ydist>=float(maze.getHeight())/2.0:
                flag = False
            
        self._start = pt1
        self._end = pt2    

