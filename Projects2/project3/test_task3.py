import labyrinth
import numpy as np
import pytest
from labyrinth import InvalidSquareError
from maze_walker import MazeWalker


class TestRNG:
    """Mock pRNG"""

    def __init__(self, seed: int = 42):
        pass

    def integers(self, min: int, max: int, size: int) -> np.ndarray:
        return np.ones(size, dtype=int)


@pytest.fixture
def rng():
    return np.random.default_rng(1910)


@pytest.fixture
def maze():
    return labyrinth.example()


@pytest.fixture
def circle():
    return labyrinth.circular()


def test_3a_properties(rng, maze):
    """Testing that properties are implemented without setters"""
    assert hasattr(MazeWalker, "M"), "property M missing"
    assert hasattr(MazeWalker, "maze"), "property labyrinth missing"
    M = 10
    walkers = MazeWalker(M, maze, rng)
    assert walkers.M == M
    assert walkers.maze is maze
    with pytest.raises(AttributeError):
        walkers.M = 3
    with pytest.raises(AttributeError):
        walkers.maze = None


@pytest.mark.parametrize("M, x0, y0", [(10, 1, 1), (13, 2, 1), (4, 2, 1)])
def test_3b_x_and_y(M, x0, y0, rng, maze):
    walkers = MazeWalker(M, maze, rng, r0=(x0, y0))
    assert np.all(walkers.x == x0)
    assert np.all(walkers.y == y0)
    assert len(walkers.x) == M
    assert len(walkers.y) == M


@pytest.mark.parametrize("r0", [(-1, 1), (2, -3), (0, 0), (2, 4)])
def test_3c_invalid_startpoint_raises_error(r0, rng, maze):
    with pytest.raises(InvalidSquareError):
        MazeWalker(10, maze, rng, r0=r0)
    mz = MazeWalker(10, maze, rng)
    with pytest.raises(InvalidSquareError):
        mz.initialize_walkers(r0)


@pytest.mark.parametrize("r0", [(100, 100), (150, 25), (33, 170)])
def test_3d_move(r0, circle):
    walkers = MazeWalker(10, circle, TestRNG(), r0=r0)
    for n in range(1, 5):
        walkers.move()
        assert np.all(walkers.x == n + r0[0])
        assert np.all(walkers.y == n + r0[1])


def test_3f_move_with_walls(rng, maze):
    walkers = MazeWalker(10, maze, rng)
    for n in range(5):
        walkers.move()
        legal = maze[walkers.x, walkers.y]
        assert np.all(legal)


@pytest.mark.parametrize("dn", [5, 1, 0])
def test_3g_not_finished(dn, circle):
    endpoint = (100 + dn, 100 + dn)
    walkers = MazeWalker(10, circle, TestRNG(), r0=(100, 100), endpoints=[endpoint])
    for n in range(dn):
        assert np.all(walkers.not_finished()), f"error at time step {n = }"
        walkers.move()
    assert np.all(~walkers.not_finished()), f"error at time step {dn = }"


@pytest.mark.parametrize("dn", [5, 1, 0])
def test_3g_move_with_endpoint(dn, circle):
    endpoint = (100 + dn, 100 + dn)
    walkers = MazeWalker(10, circle, TestRNG(), r0=(100, 100), endpoints=[endpoint])
    for n in range(1, dn + 1):
        walkers.move()
        assert np.all(walkers.x == 100 + n), f"error at time step {n = }"
        assert np.all(walkers.y == 100 + n), f"error at time step {n = }"
    for _ in range(3):
        walkers.move()
        assert np.all(walkers.x == 100 + dn), f"error at time step {dn = }"
        assert np.all(walkers.y == 100 + dn), f"error at time step {dn = }"
