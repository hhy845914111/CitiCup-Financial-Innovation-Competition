from PricingEngine.PricingEngineFactory import PricingEngineFactory


class Option(object):

    PE_FACTORY = PricingEngineFactory()

    def __init__(self, K: float, T: float, r: float, q: float,
                 vol: float, option_type: {"call", "put"}, pricing_engine: str):
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.vol = vol
        self.option_type = option_type
        self.pricing_engine = Option.PE_FACTORY.get_pricing_engine(pricing_engine)

        self.t = None
        self.S = None

    def update_S(self, S: float) -> None:
        self.S = S

    def update_t(self, t: float) -> None:
        self.t = t

    def get_price(self) -> float:
        return self.pricing_engine.price(self)

    def get_delta(self) -> float:
        return self.pricing_engine.delta(self)

    def get_gamma(self) -> float:
        return self.pricing_engine.gamma(self)

    def get_theta(self) -> float:
        return self.pricing_engine.theta(self)

    def get_rho(self) -> float:
        return self.pricing_engine.rho(self)

    def get_vega(self) -> float:
        return self.pricing_engine.vega(self)


class EuropeanOption(Option):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AmericanOption(Option):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AsianOption(Option):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
