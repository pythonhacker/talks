emaem

# Concurrency in Python 3.0

__Anand B Pillai__ <br/>
_anandpillail@letterboxes.org_ <br/>
_@skeptichacker_ <br/>


---

## Concurrency

* Most basic form of multi-tasking
* Perform more than one task during a given time duration
* Works by allocating time slices to tasks 
* Real Life Example(s) - A drummer playing on drums, Lead Singer/Guitarist in a Band.

---

## Parallelism

* Perform more than one task at a given time
* Possible with multi-core CPUs
* Your phone can perform tasks in parallel, so can your laptop.
* Real Life Example(s) - A Printer/Xerox/Scanner machine, A modern web-browser.

---
## Types of Multitasking

* Pre-emptive: CPU manages threads priority via scheduler. Threads just run.
* Co-operative: No central mangement. Threads yield to others when they're done.
* Your laptop does the former. Almost all modern computing devices does this.
* Olden days with a single mainframe timeshare computers - People used to do latter!

---

## Python & Concurrency

* Threading
* Multiprocessing
* Concurrent futures
* Async processing
* Libraries
...

Wait.

---

## Threads

* The GIL Monster
* Doesn't allow compute threads (bytecode heavy) to truly run in parallel.
* Causes thread thrashing and priority inversion
* I/O bound threads and some libraries (numpy etc) dont have a problem.

---

## Processes

* Gets around GIL
* But avoid sharing state
* Use return values as much as possible.
* Multiprocessing manager is good - but is rather heavy.
* Funky data types for shared memory - not very useful to write complex programs.

---

## Concurrent Futures

* Multiple processes returning results in future
* Good programming paradigm for data parallel computations
* Provides same interface for threading & processes

---

## Asyncio

* New library in Python3
* Asynchronous processing via co-operative multitasking
* Single thread
* Use exotic *async* and *await* keywords
* More library support needed
* Slightly high learning curve.

---

## Compute Parallel Problems

* Perform multiple tasks on the same data set in parallel (Pipelines)
* Example - Multimedia processing. Processing a set of videos to reduce their size (encoding), plus extracting meta-data (for indexing).
* Example - Machine Learning on massive data sets. Same dataset is worked upon multiple ML algorithms in parallel.

We won't be focussing on compute parallel problems.

---

## Data Parallel Problems

* Set of problems where each element of the input data can be processed independently of others
* Ideal for parallel processing because each core can work on different data elements in parallel.
* Final output is often a combination of the individual processed output.
* Example Problems
    * __Matrix Multiplication__ - Each row of the matrix can be processed in parallel and combined to generate final matrix.
    * __Fractal Image Generation__ - Each row of the image can be generated parallely to generate final image.
    * __Puzzle Solvers__ - Multiple solvers can be run in parallel to generate single solution or a batch of solutions. E.g: Sudoku Solver, Maze Solver etc.
    * __I/O Tasks__ - Almost all tasks involing input/output on file system or network can be run in parallel. E.g: Web Crawler,

---

LET'S GO!



    
