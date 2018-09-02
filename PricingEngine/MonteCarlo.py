from math import log


def generate_sample(S, r, q, vol, T, n, count):
    dt = T / n
    diff_mat = (np.random.randn(count, n) * vol * sqrt(dt) + (r - q - vol**2 / 2) * dt).astype("float64")
    diff_mat = np.hstack([np.ones([count, 1]) * log(S) , diff_mat])
    result_mat = np.exp(diff_mat.cumsum(axis=1))
    return result_mat


def asian_value(sim_mat: np.ndarray, K: float, option_type: {"call", "put"}) -> float:
    n1, n2 = sim_mat.shape
    type_cast = lambda x: 1 if x == "call" else -1
    type_int = type_cast(option_type)
    average = np.sum(sim_mat, axis=1) / n1
    return np.sum(np.where(average * type_int > K * type_int, type_int * (average - K), 0)) / n1

