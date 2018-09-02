from math import exp as m_exp
import numpy as np
from typing import Callable, Tuple
import utils






def tree_generation(S: float, t: float, r: float, q: float, vol: float, n: int) \
        -> Tuple[np.ndarray, float, float, float, float, float]:
    dt = t / n

    u = m_exp(vol * sqrt(dt))
    d = 1 / u
    p = (m_exp((r - q) * dt) - d) / (u - d)

    tree_ar = np.zeros((n + 1, n + 1))

    # boundary condition
    tree_ar[:, n] = S * u ** np.arange(n, -1, -1) * d ** np.arange(0, n + 1, 1)
    return tree_ar, p, dt, r, u, d


def valuation(f_middle: Callable[[np.ndarray, int, int], float], tree_array: np.ndarray, *args, **kwargs) \
        -> Tuple[float, np.ndarray]:
    n1, n2 = tree_array.shape
    if n1 != n2:
        raise ValueError("tree_array shape not acceptable")

    for i in range(n1 - 2, -1, -1):
        for j in range(0, i + 1):
            tree_array[j, i] = f_middle(tree_array, j, i, *args, **kwargs)
    return tree_array[0][0], tree_array


def value_end(tree_end_col: np.ndarray, K: float, option_type: str) -> np.ndarray:
    tp_int = utils.option_type_cast(option_type)
    return np.where(tp_int * tree_end_col > tp_int * K, tp_int * (tree_end_col - K), np.zeros_like(tree_end_col))


def european_value_middle(tree_col: np.ndarray, x: int, y: int, r: float, dt: float, p: float) -> float:
    return m_exp(-r * dt) * (p * tree_col[x, y + 1] + (1 - p) * tree_col[x + 1, y + 1])


def american_value_middle(
        tree_col: np.ndarray, x: int, y: int, r: float, dt: float, p: float,
        option_type: str, K: float, S0: float, u: float, d: float) -> float:

    tp_int = utils.option_type_cast(option_type)
    return max(m_exp(-r * dt) * (p * tree_col[x, y + 1] + (1 - p) * tree_col[x + 1, y + 1]),
               max(tp_int * (S0 * u ** y * d ** x - K), 0)
               )
