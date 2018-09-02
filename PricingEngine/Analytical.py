from sympy import symbols, lambdify, ln, sqrt, simplify, diff
from sympy import exp as s_exp
from sympy.stats import Normal
from sympy.stats import P as N


def generate(save=False):
    c, p, d1, d2, S, t, K, r, vol, q = symbols('c p d1 d2 S t K r vol q')
    normal = Normal('normal', 0, 1)

    d1 = (ln(S / K) + (r - q + vol ** 2 / 2) * t) / (sqrt(t) * vol)
    d2 = d1 - sqrt(t) * vol

    c = simplify(S * s_exp(-q * t) * N(normal < d1) - K * s_exp(-r * t) * N(normal < d2))
    p = simplify(-S * s_exp(-q * t) * N(normal < -d1) + K * s_exp(-r * t) * N(normal < -d2))

    c_lambda = lambdify([S, t, K, r, vol, q], c, 'math')
    p_lambda = lambdify([S, t, K, r, vol, q], p, 'math')

    c_delta = simplify(diff(c, S))
    p_delta = simplify(diff(p, S))

    c_delta_lambda = lambdify([S, t, K, r, vol, q], c_delta, 'math')
    p_delta_lambda = lambdify([S, t, K, r, vol, q], p_delta, 'math')

    c_theta = simplify(diff(c, t))
    p_theta = simplify(diff(p, t))

    c_theta_lambda = lambdify([S, t, K, r, vol, q], c_theta, 'math')
    p_theta_lambda = lambdify([S, t, K, r, vol, q], p_theta, 'math')

    c_gamma = simplify(diff(c_delta, S))
    p_gamma = simplify(diff(p_delta, S))

    c_gamma_lambda = lambdify([S, t, K, r, vol, q], c_gamma, 'math')
    p_gamma_lambda = lambdify([S, t, K, r, vol, q], p_gamma, 'math')

    c_vega = simplify(diff(c, vol))
    p_vega = simplify(diff(p, vol))

    c_vega_lambda = lambdify([S, t, K, r, vol, q], c_vega, 'math')
    p_vega_lambda = lambdify([S, t, K, r, vol, q], p_vega, 'math')

    c_rho = simplify(diff(c, r))
    p_rho = simplify(diff(p, r))

    c_rho_lambda = lambdify([S, t, K, r, vol, q], c_rho, 'math')
    p_rho_lambda = lambdify([S, t, K, r, vol, q], p_rho, 'math')

    def fc_lambda(*args, **kwargs):
        global c_lambda
        return c_lambda(*args, **kwargs)

    def fp_lambda(*args, **kwargs):
        global p_lambda
        return p_lambda(*args, **kwargs)

    def fc_delta_lambda(*args, **kwargs):
        global c_delta_lambda
        return c_delta_lambda(*args, **kwargs)

    def fp_delta_lambda(*args, **kwargs):
        global p_delta_lambda
        return p_delta_lambda(*args, **kwargs)

    def fc_gamma_lambda(*args, **kwargs):
        global c_gamma_lambda
        return c_gamma_lambda(*args, **kwargs)

    def fp_gamma_lambda(*args, **kwargs):
        global p_gamma_lambda
        return p_gamma_lambda(*args, **kwargs)

    def fc_vega_lambda(*args, **kwargs):
        global c_vega_lambda
        return c_vega_lambda(*args, **kwargs)

    def fp_vega_lambda(*args, **kwargs):
        global p_vega_lambda
        return p_vega_lambda(*args, **kwargs)

    def fc_theta_lambda(*args, **kwargs):
        global c_theta_lambda
        return c_theta_lambda(*args, **kwargs)

    def fp_theta_lambda(*args, **kwargs):
        global p_theta_lambda
        return p_theta_lambda(*args, **kwargs)

    def fc_rho_lambda(*args, **kwargs):
        global c_rho_lambda
        return c_rho_lambda(*args, **kwargs)

    def fp_rho_lambda(*args, **kwargs):
        global p_rho_lambda
        return p_rho_lambda(*args, **kwargs)

    price = {
        "call": fc_lambda,
        "put": fp_lambda,
    }

    greeks = {
        "call": {
            "delta": fc_delta_lambda,
            "gamma": fc_gamma_lambda,
            "theta": fc_theta_lambda,
            "rho": fc_rho_lambda,
            "vega": fc_vega_lambda,
        },
        "put": {
            "delta": fp_delta_lambda,
            "gamma": fp_gamma_lambda,
            "theta": fp_theta_lambda,
            "rho": fp_rho_lambda,
            "vega": fp_vega_lambda,
        }
    }

    european_option = {"price": price, "greeks": greeks}

    if save:
        import pickle as pkl

        with open("./bin/european_option.lib", "wb") as fp:
            pkl.dump(european_option, fp)

    return european_option
