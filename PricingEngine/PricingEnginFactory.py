import PricingEngine as PE


class PricingEnginFacotry(object):

    NAME_CAST = {
        "analytical": PE.AnalyticalPricingEngine,
        "binomial": PE.BinomialPricingEngine,
        "MonteCarlo": PE.MonteCarloPricingEngine
    }

    @staticmethod
    def get_pricing_engine(name: str, *args, **kwargs) -> PE.PricingEngines:
        try:
            return PricingEnginFacotry.NAME_CAST[name]()
        except KeyError:
            raise KeyError("Pricing engine not found")