# H25_project1_philipef_stanisok
Project 1 for philipef (philipef@mail.uio.no) and stanisok (stanisok@mail.uio.no) and susanhop (susanhop@mail.uio.no)

URL to GitHub: https://github.uio.no/IN1910/H25_project1_philipef_stanisok_susanhop


Exercise 2g Question:
    Is the energy conserved?
Answer:
    Yes, the energy is conserved, because the potential and kinetic energies oscillate, but the total energy curve stays essentially flat.Any tiny deviations are due to numerical errors from the solver and finite-difference velocity calculation
Exercise 2h Question:
    How does the energy compared to the energy that you plotted in Exercise 2d?
Answer:
    - The energy in the undamped 2d is nearly conserved for the whole duration, but in the dampened 2h solution it looks like it gets halved for each time point, that leads me to believe it is decreasing in exponential time.



## What this project contains
Code files:
    - ode.py - Base ODE interface (ODEModel), ODEResult, reusable plot_energy function (duck-typed)
    - exp_decay.py - Exponential decay model and example usage.
    - pendulum.py - Single pendulum model, PendulumResults dataclass, energy methods and lastly example scripts producing .png files of the plot().
    - double_pendulum.py - Double pendulum model, DoublePendulumResults dataclass, energy methods, example script for producing .png files of the plot().

Test files:
    - test_exp_decay.py - Unit tests for exponential decay ODE (RHS, solve, timings, accuracy).
    - test_pendulum.py - Parametrized tests for single pendulum object (RHS, invariants, energy methods, plotting figure to file or display).
    - test_double_pendulum.py - Parametrized tests for double pendulum derivatives and zero-IC behavior.

Figures (made by scripts in code files):
    - exponential_decay.png
    - exercise_2b.png
    - energy_single.png
    - energy_damped.png
    - energy_double.png

A .gitignore file for the Python project.


## How to run the files:
Exponential decay example:
    python exp_decay.py

Single pendulum:
    python pendulum.py

Double pendulum:
    python double_pendulum.py

Tests:
To run all tests:
    pytest -q

To run test_exp_decay:
    pytest test_exp_decay

To run test_pendulum:
    pytest test_pendulum

To run test_double_pendulum:
    pytest test_double_pendulum

## Notes on Documentation
For improved clarity, we used ChatGPT to help generate docstrings at the start of the code files and some of the docstrings. We reviewed and edited the text and formulaes so that it would be correct according to the assignment text. 
We used this assistance mainly to bridge the gap between the heavy mathematical notation and terminology, since we found it challenging to explain these aspects in a easy to understand manner.
