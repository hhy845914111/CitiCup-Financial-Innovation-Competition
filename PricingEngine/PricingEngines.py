import BinTree as BT
import MonteCarlo as MT


class PricingEngine(object):

    def price(self, option_obj) -> float:
        pass

    def delta(self, option_obj) -> float:
        pass

    def gamma(self, option_obj) -> float:
        pass

    def theta(self, option_obj) -> float:
        pass

    def rho(self, option_obj) -> float:
        pass

    def vega(self, option_obj) -> float:
        pass


class AnalyticalPricingEngine(PricingEngine):

    def __init__(self):
        import pickle as pkl

        with open("./PricingEngine/european_option.lib", "rb") as fp:
            self.analytic_dct = pkl.load(fp)

    def price(self, option_obj) -> float:
        return self.analytic_dct["price"][option_obj.option_type](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )

    def delta(self, option_obj) -> float:
        return self.analytic_dct["greeks"][option_obj.option_type]["delta"](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )

    def gamma(self, option_obj) -> float:
        return self.analytic_dct["greeks"][option_obj.option_type]["gamma"](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )

    def theta(self, option_obj) -> float:
        return self.analytic_dct["greeks"][option_obj.option_type]["theta"](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )

    def rho(self, option_obj) -> float:
        return self.analytic_dct["greeks"][option_obj.option_type]["rho"](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )

    def vega(self, option_obj) -> float:
        return self.analytic_dct["greeks"][option_obj.option_type]["vega"](
            option_obj.S,
            option_obj.T - option_obj.t,
            option_obj.K,
            option_obj.r,
            option_obj.vol,
            option_obj.q
        )


class BinomialTreePricingEngine(PricingEngine):

    def __init__(self):
        self.tree_lst = []












