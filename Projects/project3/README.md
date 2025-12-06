# H25_project3_philipef_stanisok_susanhop

Project 3 for philipef (philipef@mail.uio.no) and stanisok (stanisok@mail.uio.no) and susanhop (susanhop@mail.uio.no)

## Task 1C

Mean displacement at time step $n$ is given by

$$
    \langle x_n \rangle
    = \langle x_{n-1} + \Delta x_n \rangle
    = \langle x_{n-1} \rangle + \langle \Delta x_n \rangle
$$

Since $\Delta x_n$ has an equal chance of being -1, 0, or 1

$$
    \langle \Delta x_n \rangle
    = \frac{1}{3} \cdot (-1) + \frac{1}{3} \cdot 0 + \frac{1}{3} \cdot 1
    = 0
$$

Which means that

$$
    \langle x_n \rangle
    = \langle x_{n-1} \rangle
    = \langle x_0 \rangle
    = 0
$$

while the RMS is given by

$$
    \sqrt{\langle x_n^2 \rangle}
    = \sqrt{\langle (x_{n-1} + \Delta x_n)^2 \rangle}
    = \sqrt{\langle x_{n-1}^2 + x_{n-1}\cdot\Delta x_n + \Delta x_n^2\rangle}
    = \sqrt{\langle x_{n-1}^2 \rangle + \langle x_{n-1}\cdot\Delta x_n \rangle + \langle\Delta x_n^2\rangle}
$$

Where, because $x_{n-1}$ and $\Delta x_n$ are independent (the direction next step doesn't care what your position is at all),

$$
    \langle x_{n-1}\cdot\Delta x_n \rangle
    = \langle x_{n-1} \rangle\cdot\langle\Delta x_n\rangle
    = 0 \cdot 0 = 0
$$

The third term is

$$
    \langle\Delta x_n^2\rangle
    = \frac{1}{3} \cdot (-1)^2 + \frac{1}{3} \cdot 0^2 + \frac{1}{3} \cdot 1^2
    = \frac{1}{3} + \frac{1}{3}
    = \frac{2}{3}
$$

What we have now is

$$
    \langle x_n^2 \rangle
    = \langle x_{n-1}^2 \rangle + \frac{2}{3}
    = \langle x_0^2 \rangle + n\cdot\frac{2}{3}
    = n\cdot\frac{2}{3}
$$

Therefore the RMS is

$$
    \sqrt{\langle x_n^2 \rangle}
    = \sqrt{n\cdot\frac{2}{3}}
$$

## Task 1d

As the number of walkers M increases, the mean and RMS from the simulations approach the analytical curves more closely.
For small M's, random fluctuations dominates the plot, thereby causing visible rise.
For larger walks, the simulated mean remains near zero and the RMS follows the sqrt(2/3) line near perfectly.

## Task 2c

We write the 2D random walk as

$$
\vec r_n = \vec r_{n-1} + \Delta \vec r_n, \qquad
\vec r_0 = (0,0),
$$

with

$$
\Delta \vec r_n = (\Delta x_n, \Delta y_n), \qquad
\Delta x_n, \Delta y_n \in \\{-1, 0, 1\\},
$$

and the x- and y-steps are independent and identically distributed.

Since

$$
\langle \Delta x_n \rangle = \langle \Delta y_n \rangle = \tfrac{1}{3}(-1) + \tfrac{1}{3}(0) + \tfrac{1}{3}(1) = 0,
$$

we obtain

$$
\langle x_n \rangle = 0, \qquad \langle y_n \rangle = 0,
$$

and therefore

$$
\langle \vec r_n \rangle = (0, 0).
$$

From the 1D case we have that

$$
\langle x_n^2 \rangle = \frac{2}{3}n.
$$

By symmetry the same holds for $y_n$

$$
\langle y_n^2 \rangle = \frac{2}{3}n.
$$

Thus

$$
\langle |\vec r_n|^2 \rangle
= \langle x_n^2 \rangle + \langle y_n^2 \rangle
= \frac{2}{3}n + \frac{2}{3}n
= \frac{4}{3}n,
$$

and the RMS distance from the origin is

$$
\sqrt{\langle |\vec r_n|^2 \rangle} = \sqrt{\frac{4}{3}n}.
$$

## Task 2d

At n = 500, the points are roughly centered around the origin position (0,0), which is expected given the analytical mean $\langle \vec r_n \rangle = (0, 0).$ The spread of the cloud reflects the RMS distance growing with $\sqrt{\frac{4}{3}n}.$

## Task 3h

In task 3h, with 100000 walkers and 2000 time steps, 2675 walkers reached an endpoint.

![_](3h.png)

## Task 4a

When running the maze walker program, the move() function performs the following operations for each time step:

1. It generates N number of random steps for all M walkers.
2. It checks M position tuples to see if it is a valid move.
3. It then updates the M walkers using boolean indexing computed from the legal moves computation.

Each of these three operations on the maze walker instance scales linearly with the number of walkers M. That means the computational work per time step increases proportionally with M.

The time complexity of a single step is in O(M). Note, that the meaning of single step, means that we never enter a loop inside the move() function.
On the other hand, when we run the simulation for N steps, it will grow linearly with M and N. That means, the time complexity for N=1000 steps is: O(N \* M).

This is reasonable considering the displayed plot and '4a.png' we get from running the 'time_complexity_mw.py' source file.

## Task 4b

In this task we profiled the maze walker using: "python -m cProfile -o maze.cprof maze_walker.py".
We ran the 'maze_walker.py' file without any plotting or animation.
The profile output had these characteristics:

- Total calls: 1 157 177.
- Total time: 0.520 s.
- Most of the top entries (ranked by cumtime) were imports.
- Ordered by cumulative time, because that tells us what dominates the total runtime.

### 1. Difference between tottime and cumtime

- tottime is the time spent only inside that function itself, excluding any time in functions that gets called from it.
- cumtime (cumulative time) includes the time spent in that function and in all the functions it calls.

They will be the same when a function performs all of its work internally (does not call other functions). They will differ when a function that imports or delegates work to other functions.
An example of this from the cProfile output is:

- cumtime: 0.001, tottime: 0.458, &lt;frozen importlib.\_bootstrap&gt;:1349(\_find_and_load)
- cumtime: 0.001, tottime: 0.458, &lt;frozen importlib.\_bootstrap&gt;:1304(\_find_and_load_unlocked)

They have small tottime but large cumtime, because they call many other functions during module imports.

### 2. Functions consuming the most time.

Based on the output from 'maze.cprof':
| Rank | Function | tottime (s) | cumtime (s) |
| ---- | -------- | ----------- | ----------- |
| 1 | &lt;frozen importlib.\_bootstrap&gt;:1349(\_find_and_load) | 0.001 | 0.458 |
| 2 | &lt;frozen importlib.\_bootstrap&gt;:1304(\_find_and_load_unlocked) | 0.001 | 0.458 |
| 3 | &lt;frozen importlib.\_bootstrap&gt;:911(\_load_unlocked) | 0.001 | 0.457 |

These three functions show up high, because on the first run of the program, Python imports matplotlib via the labyrinth.py file and other functions (one-time cost, but still expensive compared to the rest for the small N and M).
So, even though we removed the animation and plotting, it still takes quite a bit of time.
Our own functions like the MazeWalker.move() and \_remove_illegal() do not even show up in the top 20 cumulative time entries.
Since we want to know which parts dominate the total runtime, it makes more sense here to look at cumulative time instead of total time.

### 3. Suggested changes to make it faster

From the cProfile output results, we can suggest:

1. Avoid importing Matplotlib in labyrinth.py. By either removing or encapsulating the import to only be enacted when necessary would be for the best to avoid the startup imports taking up the majority of the top 20 in relation to cumtime.
2. We should avoid making new temporary arrays in \_remove_illegal() function and rather have one on initialization that gets cleaned up during runs when that is possible.
3. When checking the out of bounds and wall coordinate moves we do some operations that also make temporary arrays. I am not sure how it could be optimized, but there should be some better ways to this, but I do not know of any.
4. In the not_finished() function we do a explicit and relatively computationally "hard" == chack and AND operator check to make sure the endpoints are in the end position. Using an np.ndarray that is vectorized might be better. Could also use a better datastructure for comparisons like a hashmap.
5. In the move() function we could change it to generate random integers after we know that the coordinate is not an end point, thereby avoiding generating them for end points and just continuing with the next coordinates!
6. In the \_remove_illegal() function we compute the nrows and ncols every iteration, which will be computationally expensive when the number of iterations increases. Might be good to initialize a grid once and reuse it somehow.
