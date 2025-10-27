Forelesning 19 - Prosjekt 3 start

MD working for project?:

Mean displacement at time step $n$ is given by

$$
    \langle x_n \rangle
    = \langle x_{n-1} + \Delta x_n \rangle
    = \langle x_n \rangle
    = \langle x_{n-1} \rangle
$$

Since $\Delta x_n$ has an equal chance of being -1, 0, or 1

$$
    \langle \Delta x_n \rangle
    = \frac{1}{3} \cdot (-1) + \frac{1}{3} \cdot 0 + \frac{1}{3} \cdot 1
    = 0
$$

Which means that

$$
    \langle x_n \rangle = \langle x_{n-1} \rangle = \langle x_0 \rangle = 0
$$

while the RMS is given by

$$
    \sqrt{\langle x_n^2 \rangle}
    = \sqrt{\langle x_{n-1} + \Delta x_n^2 \rangle}
    = \sqrt{\langle x_{n-1}^2 + x_{n-1}\cdot\Delta x_n + \Delta x_n^2\rangle}
    = \sqrt{\langle x_{n-1}^2 \rangle + \langle x_{n-1}\cdot\Delta x_n \rangle + \langle\Delta x_n^2\rangle}
$$

Where, because $x_{n-1}$ and &\Delta x_n$ are independent (the direction next step doesnt care what your position is at all),

$$
    \langle x_{n-1}\cdot\Delta x_n \rangle
    = \langle x_{n-1} \rangle\cdot\langle\Delta x_n\rangle = 0
    = 0 \cdot 0 = 0
$$

The third term is

$$
    \langle\Delta x_n^2\rangle
    = \frac{1}{3} \cdot (-1)^2 + \frac{1}{3} \cdot 0^2 + \frac{1}{3} \cdot 1^2
    = \frac{1}{3} + \frac{1}{3}
    = \frac{2}{3}
$$
