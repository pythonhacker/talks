
__Concurrency in Python 3.0 - Oh my!__

__Anand B Pillai__ <br/>
_anandpillail@letterboxes.org_ <br/>
_@skeptichacker_ <br/>


---

__Concurrency__

* Perform more than one task at a given time
* Tasks may be running truly in parallel or not.
* Example - A runner running and jumping over hurdles.

---

__Parallelism__

* Perform more than one task - truly parallel
* Truly possible with multiple core CPUs.
* Example - A footballer running and moving the ball with him.

* Data Parallel - Most common, split a series of data to multiple tasks doing same thing and combine results.
* Compute Parallel - Perform multiple tasks on the same data set in parallel (Pipelines)

---

__Analogies__

__Painting your house__

* Paint with 1 painter - Serial (no concurrency)
* Paint with 1 painter painting one room in morning and another in afternoon - concurrent
* Paint with 2 painters paiting 2 rooms in parallel - truly parallel

---
__Types of Multitasking__

* Pre-emptive: CPU manages threads priority via scheduler. Threads just run.
* Co-operative: No central mangement. Threads yield to others when they're done.

* Your laptop does the former.
* Olden days with a single mainframe timeshare computers - People used to do latter!

---

__Python & Concurrency__

* Threading
* Multiprocessing
* Concurrent futures
* Async processing
* Libraries
* Oh my!...

Wait.

---

__Threads__

* The GIL Monster
* Doesn't allow compute threads (bytecode heavy) to truly run in parallel.
* Causes thread thrashing and priority inversion
* I/O bound threads and some libraries (numpy etc) dont have a problem.

---
__Processes__

* Gets around GIL
* But avoid sharing state
* Use return values as much as possible.
* Multiprocessing manager is good - but is rather heavy.
* Funky data types for shared memory - not very useful to write complex programs.

---
__Concurrent Futures__

* Multiple processes returning results in future
* Good programming paradigm for data parallel computations
* Provides same interface for threading & processes

---
__Asyncio__

* New library in Python3
* Exotic
* Asynchronous processing via co-operative multitasking
* Single thread
* Use exotic *async* and *await* keywords
* More library support needed
* Slightly high learning curve.

---
__Async Libraries__

* Twisted - Reactor pattern, uses deferreds with callback chains.
** Deferreds are like futures.
* Gevent & Eventlet - Asynchronous processing libraries.
** Slightly old story now a days, still interesting to give a try.
** Uses greenlets - microthreads which use a kind of cooperative multitasking.

---

__Examples__

---

    >>> import antigravity
	
