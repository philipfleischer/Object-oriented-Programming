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
    = \sqrt{\langle (x_{n-1} + \Delta x_n)^2 \rangle}
    = \langle \rangle
$$
