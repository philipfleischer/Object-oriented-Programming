Forelesning 19 - Prosjekt 3 start

MD working for project?:

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

Here comes project 3 testing:

### Analytical statistical properties (2D)

We write the 2D random walk as

$$
\vec r_n = \vec r_{n-1} + \Delta \vec r_n, \qquad
\vec r_0 = (0,0),
$$

with

$$
\Delta \vec r_n = (\Delta x_n, \Delta y_n), \qquad
\Delta x_n, \Delta y_n \in \{-1, 0, 1\},
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

From the 1D case we had

$$
\langle x_n^2 \rangle = \frac{2}{3}n.
$$

By symmetry the same holds for \(y_n\):

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
